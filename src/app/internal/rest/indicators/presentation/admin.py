from django.contrib import admin

from app.internal.rest.indicators.db.models import *


@admin.register(Humidity)
class HumidityAdmin(admin.ModelAdmin):
    pass


@admin.register(ReedSensor)
class ReedSensorAdmin(admin.ModelAdmin):
    pass


@admin.register(HydrogenIndicator)
class HydrogenIndicatorAdmin(admin.ModelAdmin):
    pass


@admin.register(Illumination)
class IlluminationAdmin(admin.ModelAdmin):
    pass


@admin.register(SolutionConductivity)
class SolutionConductivityAdmin(admin.ModelAdmin):
    pass


@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    pass

@admin.register(Soil)
class SoilAdmin(admin.ModelAdmin):
    pass