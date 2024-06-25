from ninja import NinjaAPI

from app.internal.rest.indicators.presentation.handlers import IndicatorsHandler
from app.internal.rest.indicators.presentation.routes import add_indicators_router
from app.internal.rest.indicators.domain.service import IndicatorsService


def add_indicators_api(api: NinjaAPI):
    indicators_service = IndicatorsService()
    indicators_handler = IndicatorsHandler(indicators_service)
    add_indicators_router(api, indicators_handler)
