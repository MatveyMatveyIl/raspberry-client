from ninja import NinjaAPI, Router

from app.internal.rest.microclimate.domain.entities import ClimateScheduleSchema, ClimateMode, ClimateDTO
from app.internal.rest.microclimate.presentation.handlers import ClimateHandler


def get_climate_router(climate_handler):
    router = Router(tags=["climate"])

    router.add_api_operation(
        "/schedules",
        ["PATCH"],
        climate_handler.update_climate_schedule,
        response={201: ClimateScheduleSchema}
    )

    router.add_api_operation(
        "/schedules",
        ["GET"],
        climate_handler.get_climate_schedule,
        response={200: ClimateScheduleSchema}
    )

    router.add_api_operation(
        "/mode",
        ["PATCH"],
        climate_handler.update_work_mode,
        response={201: ClimateMode}
    )

    router.add_api_operation(
        "/mode",
        ["GET"],
        climate_handler.get_work_mode,
        response={200: ClimateMode}
    )

    router.add_api_operation(
        "/",
        ["PATCH"],
        climate_handler.update_climate,
        response={201: ClimateDTO}
    )

    router.add_api_operation(
        "/",
        ["GET"],
        climate_handler.get_climate,
        response={200: ClimateDTO}
    )

    return router


def add_climate_router(api: NinjaAPI, climate_handler: ClimateHandler):
    climate_routes = get_climate_router(climate_handler)
    api.add_router("/climate", climate_routes)
