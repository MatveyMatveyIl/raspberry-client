from ninja import NinjaAPI

from app.internal.rest.indicators.app import add_indicators_api
from app.internal.rest.light.app import add_light_api
from app.internal.rest.microclimate.app import add_climate_api
from app.internal.rest.irrigation.app import add_irrigation_api
from app.internal.rest.camera.app import add_camera_api


def get_api():
    api = NinjaAPI(title="Raspberry", version="1.0.0")
    add_indicators_api(api)
    add_light_api(api)
    add_climate_api(api)
    add_irrigation_api(api)
    add_camera_api(api)
    return api


ninja_api = get_api()
