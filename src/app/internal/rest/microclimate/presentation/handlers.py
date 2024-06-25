from ninja import Body

from app.internal.rest.microclimate.domain.entities import ClimateScheduleIn, ClimateDTO, ClimateMode, \
    ClimateScheduleSchema
from app.internal.rest.microclimate.domain.service import ClimateService


class ClimateHandler:
    def __init__(self, climate_service: ClimateService):
        self.climate_service = climate_service

    def update_climate_schedule(self, request, body: ClimateScheduleIn = Body(...)):
        schedule = self.climate_service.update_climate_schedule(**dict(body))
        return 201, ClimateScheduleSchema.from_orm(schedule)

    def get_climate_schedule(self, request):
        schedule = self.climate_service.get_schedule()
        return 200, ClimateScheduleSchema.from_orm(schedule)

    def update_work_mode(self, request, body: ClimateMode = Body(...)):
        mode = self.climate_service.change_mod(**dict(body))
        return 201, ClimateMode(mode=mode)

    def get_work_mode(self, request):
        mode = self.climate_service.get_mode()
        return 200, ClimateMode(mode=mode)

    def update_climate(self, request, body: ClimateDTO = Body(...)):
        climate = self.climate_service.update_climate(**dict(body))
        return 201, ClimateDTO(work_type=climate.work_type)

    def get_climate(self, request):
        climate = self.climate_service.get_climate()
        return 200, ClimateDTO(work_type=climate.work_type)
