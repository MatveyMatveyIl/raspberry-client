from django.contrib import admin

from app.internal.rest.microclimate.db.models import Climate, ClimateSchedule, ClimateState


@admin.register(Climate)
class ClimateAdmin(admin.ModelAdmin):
    pass


@admin.register(ClimateState)
class ClimateStateAdmin(admin.ModelAdmin):
    pass


@admin.register(ClimateSchedule)
class ClimateScheduleAdmin(admin.ModelAdmin):
    pass
