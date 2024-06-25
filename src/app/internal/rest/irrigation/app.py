from ninja import NinjaAPI

from app.internal.rest.irrigation.domain.service import IrrigationService
from app.internal.rest.irrigation.presentation.handlers import IrrigationHandler
from app.internal.rest.irrigation.presentation.routes import add_irrigation_router


def add_irrigation_api(api: NinjaAPI):
    irrigation_service = IrrigationService()
    irrigation_handler = IrrigationHandler(irrigation_service)
    add_irrigation_router(api, irrigation_handler)
