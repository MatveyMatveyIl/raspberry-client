from decimal import Decimal
from uuid import UUID

from app.internal.rest.irrigation.db.models import IrrigationSchedule, Irrigation, IrrigationModeType, IrrigationState


class IrrigationService:
    def add_irrigation_schedule(self, time_start: str, duration: Decimal, power: int):
        duration = duration % 86400
        schedule = IrrigationSchedule.objects.create(
            time_start=time_start,
            duration=duration,
            power=power
        )
        return schedule

    def get_schedules(self):
        schedules = IrrigationSchedule.objects.order_by("time_start").all()
        return schedules

    def delete_schedule(self, id: UUID):
        IrrigationSchedule.objects.filter(id=id).delete()

    def change_mod(self, mode: IrrigationModeType):
        state = IrrigationState.objects.first()
        state.mode = mode
        state.save()
        return state.mode

    def get_mode(self):
        return IrrigationState.objects.first().mode

    def update_irrigation(self, power: int):
        irrigation = Irrigation.objects.first()
        irrigation.power = power
        irrigation.save()
        return irrigation

    def get_irrigation(self):
        return Irrigation.objects.first()

    def init_values(self):
        if IrrigationState.objects.count() == 0:
            IrrigationState.objects.create(mode=IrrigationModeType.off)
        if Irrigation.objects.count() == 0:
            Irrigation.objects.create(power=0)
