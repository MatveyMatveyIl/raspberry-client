from app.internal.rest.indicators.db.models import (
    Humidity,
    HydrogenIndicator,
    Illumination,
    Temperature,
    SolutionConductivity,
    ReedSensor,
    Soil
)
from app.internal.rest.indicators.domain.entities import IndicatorOut, IndicatorsValuesOut


class IndicatorsService:

    def get_indicators(self):

        hum = self.get_humidity()
        hyd = self.get_hydrogen_indicator()
        ill = self.get_illumination()
        sol = self.get_solution_conductivity()
        temp = self.get_temperature()
        reed = self.get_reed_sensor()
        soil = self.get_soil()

        return IndicatorsValuesOut(humidity=hum, hydrogen=hyd, illumination=ill, temperature=temp,
                                   solution_conductivity=sol, reed_sensor=reed, soil=soil)

    def get_humidity(self):
        indicator = Humidity.objects.order_by("-time").first()
        if indicator is None:
            return IndicatorOut(indication="error")
        return IndicatorOut(indication=indicator.indication)

    def get_hydrogen_indicator(self):
        indicator = HydrogenIndicator.objects.order_by("-time").first()
        if indicator is None:
            return IndicatorOut(indication="error")
        return IndicatorOut(indication=indicator.indication)

    def get_illumination(self):
        indicator = Illumination.objects.order_by("-time").first()
        if indicator is None:
            return IndicatorOut(indication="error")
        return IndicatorOut(indication=indicator.indication)

    def get_solution_conductivity(self):
        indicator = SolutionConductivity.objects.order_by("-time").first()
        if indicator is None:
            return IndicatorOut(indication="error")
        return IndicatorOut(indication=indicator.indication)

    def get_temperature(self):
        indicator = Temperature.objects.order_by("-time").first()
        if indicator is None:
            return IndicatorOut(indication="error")
        return IndicatorOut(indication=indicator.indication)

    def get_reed_sensor(self):
        indicator = ReedSensor.objects.order_by("-time").first()
        if indicator is None:
            return IndicatorOut(indication="error")
        return IndicatorOut(indication=indicator.indication)

    def get_soil(self):
        indicator = Soil.objects.order_by("-time").first()
        if indicator is None:
            return IndicatorOut(indication="error")
        return IndicatorOut(indication=indicator.indication)

    def init_values(self):
        if Illumination.objects.count() == 0:
            Illumination.objects.create(indication="777")
        if Temperature.objects.count() == 0:
            Temperature.objects.create(indication="23")
        if Humidity.objects.count() == 0:
            Humidity.objects.create(indication="45")
        if HydrogenIndicator.objects.count() == 0:
            HydrogenIndicator.objects.create(indication="7.9")
        if SolutionConductivity.objects.count() == 0:
            SolutionConductivity.objects.create(indication="0.5")
        if ReedSensor.objects.count() == 0:
            ReedSensor.objects.create(indication="Пустой")
        if Soil.objects.count() == 0:
            Soil.objects.create(indication="1")
