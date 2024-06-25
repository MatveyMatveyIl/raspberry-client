from uuid import UUID

from ninja import Body, Path

from app.internal.rest.irrigation.domain.entities import IrrigationScheduleIn, IrrigationIn, IrrigationMode, \
    IrrigationScheduleSchema, IrrigationSchedules, IrrigationSchema
from app.internal.rest.irrigation.domain.service import IrrigationService
from app.pkg.responses import SuccessResponse


class IrrigationHandler:
    def __init__(self, irrigation_service: IrrigationService):
        self.irrigation_service = irrigation_service

    def add_irrigation_schedule(self, request, body: IrrigationScheduleIn = Body(...)):
        schedule = self.irrigation_service.add_irrigation_schedule(**dict(body))
        return 201, IrrigationScheduleSchema.from_orm(schedule)

    def get_irrigation_schedules(self, request):
        schedules = self.irrigation_service.get_schedules()
        schedules_out = [IrrigationScheduleSchema.from_orm(el) for el in schedules]
        return 200, IrrigationSchedules(schedules=schedules_out)

    def delete_schedule(self, request, path: UUID = Path(...)):
        self.irrigation_service.delete_schedule(path)
        return 201, SuccessResponse()

    def update_work_mode(self, request, body: IrrigationMode = Body(...)):
        mode = self.irrigation_service.change_mod(**dict(body))
        return 201, IrrigationMode(mode=mode)

    def get_work_mode(self, request):
        mode = self.irrigation_service.get_mode()
        return 200, IrrigationMode(mode=mode)

    def update_irrigation(self, request, body: IrrigationIn = Body(...)):
        irrigation = self.irrigation_service.update_irrigation(**dict(body))
        return 201, IrrigationSchema.from_orm(irrigation)

    def get_irrigation(self, request):
        irrigation = self.irrigation_service.get_irrigation()
        return 200, IrrigationSchema.from_orm(irrigation)
