from ninja import Schema
from ninja.orm import create_schema

from app.internal.rest.light.db.models import LightModeType, LightSchedule, Light

LightScheduleSchema = create_schema(LightSchedule)
LightSchema = create_schema(Light)


class LightScheduleIn(Schema):
    R_channel: int
    G_channel: int
    B_channel: int
    time_start: str
    time_end: str


class LightMode(Schema):
    mode: LightModeType


class LightIn(Schema):
    R_channel: int
    G_channel: int
    B_channel: int
