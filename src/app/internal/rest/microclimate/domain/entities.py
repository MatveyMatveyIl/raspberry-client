from decimal import Decimal

from ninja import Schema
from ninja.orm import create_schema

from app.internal.rest.microclimate.db.models import WorkType, ClimateModeType, ClimateSchedule

ClimateScheduleSchema = create_schema(ClimateSchedule)


class ClimateScheduleIn(Schema):
    t_max: Decimal
    t_necessary: Decimal
    t_min: Decimal


class ClimateMode(Schema):
    mode: ClimateModeType


class ClimateDTO(Schema):
    work_type: WorkType
