from ninja import Schema


class IndicatorOut(Schema):
    indication: str


class IndicatorsValuesOut(Schema):
    humidity: IndicatorOut = None
    hydrogen: IndicatorOut = None
    illumination: IndicatorOut = None
    temperature: IndicatorOut = None
    solution_conductivity: IndicatorOut = None
    reed_sensor: IndicatorOut = None
    soil: IndicatorOut = None


class IndicatorsOut(Schema):
    indicators: IndicatorsValuesOut
