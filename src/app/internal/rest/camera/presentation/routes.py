from ninja import NinjaAPI, Router

from app.internal.rest.camera.domain.entities import CameraImageSchema
from app.internal.rest.camera.presentation.handlers import CameraHandler


def add_camera_router(api: NinjaAPI, camera_handler: CameraHandler):
    camera_router = get_camera_router(camera_handler)
    api.add_router("/camera", camera_router)


def get_camera_router(camera_handler):
    router = Router(tags=["camera"])

    router.add_api_operation(
        "/",
        ["GET"],
        camera_handler.get_image,
        response={200: CameraImageSchema},
    )

    return router
