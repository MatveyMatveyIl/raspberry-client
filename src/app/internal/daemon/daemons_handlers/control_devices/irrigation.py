import importlib.util
import time
from datetime import datetime, timedelta

from app.internal.daemon.daemons_handlers.control_devices.PIN_settings import *
from app.internal.rest.indicators.db.models import ReedSensor
from app.internal.rest.irrigation.db.models import IrrigationSchedule, IrrigationState, IrrigationModeType, Irrigation
from pydub import AudioSegment
from pydub.playback import play

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


class IrrigationDaemon:
    def __init__(self):
        self.schedules = []
        GPIO.setup(PUMP_PIN, GPIO.OUT)
        self.pump_control = GPIO.PWM(PUMP_PIN, FREQUENCY)
        self.pump_song = AudioSegment.from_mp3("src/sounds/полив.mp3")
        self.sound_activated = False

    def handle(self):
        while True:
            try:
                time.sleep(UPDATE_TIME)
                state = IrrigationState.objects.first()
                if state is None:
                    continue
                elif state.mode == IrrigationModeType.auto:
                    self._handle_auto_mode()
                elif state.mode == IrrigationModeType.manual:
                    self._handle_manual_mode()
                else:
                    self._pump_stop()
            except Exception:
                pass

    def _handle_auto_mode(self):
        self._get_light_schedule()

        if len(self.schedules) == 0:
            return

        for schedule in self.schedules:
            time_now = (datetime.now() + timedelta(hours=5)).time()
            time_start = datetime.strptime(schedule.time_start, "%H:%M")
            time_end = (time_start + timedelta(minutes=float(schedule.duration)))
            time_start = time_start.time()
            time_end = time_end.time()
            reed = ReedSensor.objects.order_by("-time").first()
            if reed.indication == "Полный":
                self._pump_stop()
                return
            if time_start <= time_now <= time_end:
                self._pump_start(schedule.power)
                return
        self._pump_stop()

    def _pump_start(self, dc: int):
        if not self.sound_activated:
            play(self.pump_song)
            self.sound_activated = True

        self.pump_control.start(dc)

    def _pump_stop(self):
        self.sound_activated = False
        self.pump_control.stop()

    def _handle_manual_mode(self):
        irrigation = Irrigation.objects.first()
        if irrigation is None:
            return

        self._pump_start(irrigation.power)

    def _get_light_schedule(self):
        schedule = IrrigationSchedule.objects.all()
        if len(schedule) != 0:
            self.schedules = [el for el in schedule]
