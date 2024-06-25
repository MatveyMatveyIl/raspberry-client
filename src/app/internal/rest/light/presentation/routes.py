from ninja import NinjaAPI, Router

from app.internal.rest.light.domain.entities import LightScheduleSchema, LightSchema, LightMode
from app.internal.rest.light.presentation.handlers import LightHandler
from app.pkg.responses import SuccessResponse


def get_light_router(light_handler):
    router = Router(tags=["light"])

    router.add_api_operation(
        "/schedules",
        ["PATCH"],
        light_handler.update_light_schedule,
        response={201: LightScheduleSchema}
    )

    router.add_api_operation(
        "/schedules",
        ["GET"],
        light_handler.get_light_schedule,
        response={200: LightScheduleSchema}
    )

    router.add_api_operation(
        "/mode",
        ["PATCH"],
        light_handler.update_work_mode,
        response={201: LightMode}
    )

    router.add_api_operation(
        "/mode",
        ["GET"],
        light_handler.get_work_mode,
        response={200: LightMode}
    )

    router.add_api_operation(
        "/",
        ["PATCH"],
        light_handler.update_light,
        response={201: LightSchema}
    )

    router.add_api_operation(
        "/",
        ["GET"],
        light_handler.get_light,
        response={200: LightSchema}
    )

    return router


def add_light_router(api: NinjaAPI, light_handler: LightHandler):
    light_routes = get_light_router(light_handler)
    api.add_router("/light", light_routes)
