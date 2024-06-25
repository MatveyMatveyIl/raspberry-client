from django.contrib import admin

from app.internal.rest.light.db.models import *


@admin.register(LightSchedule)
class LightScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(LightState)
class LightStateAdmin(admin.ModelAdmin):
    pass


@admin.register(Light)
class LightAdmin(admin.ModelAdmin):
    pass
