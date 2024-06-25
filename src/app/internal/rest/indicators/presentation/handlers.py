from app.internal.rest.indicators.domain.service import IndicatorsService

from app.internal.rest.indicators.domain.entities import IndicatorsOut


class IndicatorsHandler:
    def __init__(self, indicators_service: IndicatorsService):
        self.indicators_service = indicators_service

    def get_indicators(self, request):
        indicators = self.indicators_service.get_indicators()
        return 200, IndicatorsOut(indicators=indicators)
