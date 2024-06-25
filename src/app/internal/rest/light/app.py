from ninja import NinjaAPI

from app.internal.rest.light.domain.service import LightScheduleService
from app.internal.rest.light.presentation.handlers import LightHandler
from app.internal.rest.light.presentation.routes import add_light_router


def add_light_api(api: NinjaAPI):
    light_service = LightScheduleService()
    light_handler = LightHandler(light_service)
    add_light_router(api, light_handler)
