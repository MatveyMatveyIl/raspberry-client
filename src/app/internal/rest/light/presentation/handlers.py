from ninja import Body

from app.internal.rest.light.domain.entities import LightScheduleIn, LightMode, LightIn, LightScheduleSchema, \
    LightSchema
from app.internal.rest.light.domain.service import LightScheduleService


class LightHandler:
    def __init__(self, light_schedule_service: LightScheduleService):
        self.light_schedule_service = light_schedule_service

    def update_light_schedule(self, request, body: LightScheduleIn = Body(...)):
        schedule = self.light_schedule_service.update_light_schedule(**dict(body))
        return 201, LightScheduleSchema.from_orm(schedule)

    def get_light_schedule(self, request):
        schedule = self.light_schedule_service.get_schedule()
        return 200, LightScheduleSchema.from_orm(schedule)

    def update_work_mode(self, request, body: LightMode = Body(...)):
        mode = self.light_schedule_service.change_mod(**dict(body))
        return 201, LightMode(mode=mode)

    def get_work_mode(self, request):
        mode = self.light_schedule_service.get_mode()
        return 200, LightMode(mode=mode)

    def update_light(self, request, body: LightIn = Body(...)):
        light = self.light_schedule_service.update_light(**dict(body))
        return 201, LightSchema.from_orm(light)

    def get_light(self, request):
        light = self.light_schedule_service.get_light()
        return 200, LightSchema.from_orm(light)
