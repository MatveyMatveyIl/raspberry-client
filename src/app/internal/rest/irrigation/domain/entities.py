from decimal import Decimal
from typing import List

from ninja import Schema
from ninja.orm import create_schema

from app.internal.rest.irrigation.db.models import IrrigationModeType, IrrigationSchedule, Irrigation

IrrigationScheduleSchema = create_schema(IrrigationSchedule)
IrrigationSchema = create_schema(Irrigation)


class IrrigationScheduleIn(Schema):
    time_start: str
    duration: Decimal
    power: int


class IrrigationSchedules(Schema):
    schedules: List[IrrigationScheduleSchema]


class IrrigationMode(Schema):
    mode: IrrigationModeType


class IrrigationIn(Schema):
    power: int
