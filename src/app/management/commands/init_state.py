from django.core.management.base import BaseCommand

from app.internal.rest.camera.db.models import CameraImage
from app.internal.rest.indicators.domain.service import IndicatorsService
from app.internal.rest.irrigation.domain.service import IrrigationService
from app.internal.rest.light.domain.service import LightScheduleService
from app.internal.rest.microclimate.domain.service import ClimateService


class Command(BaseCommand):
    def handle(self, *args, **options):
        light_service = LightScheduleService()
        climate_service = ClimateService()
        irrigation_service = IrrigationService()
        indicators_service = IndicatorsService()
        light_service.init_values()
        climate_service.init_values()
        irrigation_service.init_values()
        indicators_service.init_values()
        if CameraImage.objects.count() == 0:
            CameraImage.objects.create(image_b64="")
