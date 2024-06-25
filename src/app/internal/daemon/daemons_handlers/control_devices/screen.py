import time

from app.internal.daemon.daemons_handlers.control_devices.PIN_settings import *
from app.internal.rest.indicators.db.models import *
from app.internal.rest.irrigation.db.models import IrrigationState, IrrigationModeType
from app.internal.rest.microclimate.db.models import ClimateState, ClimateModeType, Climate, WorkType

try:
    from rpi_lcd import LCD
except ImportError:
    from app.pkg.fake_lcd import LCD


class ScreenDaemon:
    def __init__(self):
        self.lcd = LCD()

    def handle(self):
        time.sleep(20)
        while True:
            try:
                time.sleep(UPDATE_TIME + 5)
                first_line, second_line = self._get_output()
                self.lcd.text(first_line, 1)
                self.lcd.text(second_line, 2)
            except Exception:
                pass

    def _get_output(self):
        temp = Temperature.objects.order_by("-time").first()
        temp = f"{temp.indication[:4]}C" if temp is not None else "err"
        hum = Humidity.objects.order_by("-time").first()
        hum = f"{int(float(hum.indication))}%" if hum is not None else "err"
        il = Illumination.objects.order_by("-time").first()
        il = f"{int(float(il.indication[:5]))}Lx" if il is not None else "err"
        sc = SolutionConductivity.objects.order_by("-time").first()
        sc = f"{sc.indication[:5]}A" if sc is not None else "err"
        ph = HydrogenIndicator.objects.order_by("-time").first()
        ph = f"{ph.indication[:4]}ph" if ph is not None else "err"
        # irrigation_state = IrrigationState.objects.first()
        # if irrigation_state.mode == IrrigationModeType.manual:
        #     return f"Irrigation T:{temp}", f"H:{hum} pH:{ph} I:{sc}"
        # climate_state = ClimateState.objects.first()
        # if climate_state.mode == ClimateModeType.manual:
        #     climate = Climate.objects.first()
        #     work_type = "Heat" if climate.work_type == WorkType.heat else "Vent"
        #     return f"{work_type} T:{temp}", f"H:{hum} Il:{il}"
        first_line = f"{hum} {temp} {sc}"
        second_line = f"{ph} {il}"
        print(first_line)
        print(second_line)
        return first_line, second_line
