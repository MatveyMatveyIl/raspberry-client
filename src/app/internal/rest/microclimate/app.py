from ninja import NinjaAPI

from app.internal.rest.microclimate.domain.service import ClimateService
from app.internal.rest.microclimate.presentation.handlers import ClimateHandler
from app.internal.rest.microclimate.presentation.routes import add_climate_router


def add_climate_api(api: NinjaAPI):
    climate_service = ClimateService()
    climate_handler = ClimateHandler(climate_service)
    add_climate_router(api, climate_handler)
