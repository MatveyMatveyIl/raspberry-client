from django.contrib import admin

from app.internal.rest.irrigation.db.models import Irrigation, IrrigationSchedule, IrrigationState


@admin.register(Irrigation)
class IrrigationAdmin(admin.ModelAdmin):
    pass


@admin.register(IrrigationState)
class IrrigationStateAdmin(admin.ModelAdmin):
    pass


@admin.register(IrrigationSchedule)
class IrrigationScheduleAdmin(admin.ModelAdmin):
    pass
