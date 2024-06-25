from ninja import NinjaAPI

from app.internal.rest.camera.presentation.handlers import CameraHandler
from app.internal.rest.camera.presentation.routes import add_camera_router


def add_camera_api(api: NinjaAPI):
    camera_handler = CameraHandler()
    add_camera_router(api, camera_handler)
