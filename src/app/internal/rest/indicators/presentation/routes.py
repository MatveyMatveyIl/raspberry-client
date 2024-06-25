from ninja import NinjaAPI, Router

from app.internal.rest.indicators.domain.entities import IndicatorsOut
from app.internal.rest.indicators.presentation.handlers import IndicatorsHandler


def add_indicators_router(api: NinjaAPI, indicator_handler: IndicatorsHandler):
    indicators_router = get_indicators_router(indicator_handler)
    api.add_router("/indicators", indicators_router)


def get_indicators_router(indicator_handler):
    router = Router(tags=["indicators"])

    router.add_api_operation(
        "/",
        ["GET"],
        indicator_handler.get_indicators,
        response={200: IndicatorsOut},
    )

    return router
