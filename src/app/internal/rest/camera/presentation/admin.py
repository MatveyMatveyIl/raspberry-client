from django.contrib import admin

from app.internal.rest.camera.db.models import *


@admin.register(CameraImage)
class CameraImageAdmin(admin.ModelAdmin):
    pass
