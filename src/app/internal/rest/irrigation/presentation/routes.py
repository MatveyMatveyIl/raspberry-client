from ninja import NinjaAPI, Router

from app.internal.rest.irrigation.domain.entities import IrrigationScheduleSchema, IrrigationSchedules, IrrigationMode, \
    IrrigationSchema
from app.internal.rest.irrigation.presentation.handlers import IrrigationHandler
from app.pkg.responses import SuccessResponse


def get_irrigation_router(irrigation_handler):
    router = Router(tags=["irrigation"])

    router.add_api_operation(
        "/schedules",
        ["PATCH"],
        irrigation_handler.add_irrigation_schedule,
        response={201: IrrigationScheduleSchema}
    )

    router.add_api_operation(
        "/schedules",
        ["GET"],
        irrigation_handler.get_irrigation_schedules,
        response={200: IrrigationSchedules}
    )

    router.add_api_operation(
        "/schedules/{path}",
        ["DELETE"],
        irrigation_handler.delete_schedule,
        response={201: SuccessResponse}
    )

    router.add_api_operation(
        "/mode",
        ["PATCH"],
        irrigation_handler.update_work_mode,
        response={201: IrrigationMode}
    )

    router.add_api_operation(
        "/mode",
        ["GET"],
        irrigation_handler.get_work_mode,
        response={200: IrrigationMode}
    )

    router.add_api_operation(
        "/",
        ["PATCH"],
        irrigation_handler.update_irrigation,
        response={201: IrrigationSchema}
    )

    router.add_api_operation(
        "/",
        ["GET"],
        irrigation_handler.get_irrigation,
        response={200: IrrigationSchema}
    )

    return router


def add_irrigation_router(api: NinjaAPI, irrigation_handler: IrrigationHandler):
    irrigation_routes = get_irrigation_router(irrigation_handler)
    api.add_router("/irrigation", irrigation_routes)
