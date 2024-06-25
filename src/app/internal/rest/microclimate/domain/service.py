from decimal import Decimal

from app.internal.rest.microclimate.db.models import *


class ClimateService:
    def update_climate_schedule(self, t_max: Decimal, t_necessary: Decimal, t_min: Decimal):
        temps = [t_max, t_min, t_necessary]
        temps.sort()
        t_min, t_necessary, t_max = temps[0], temps[1], temps[2]
        schedule = ClimateSchedule.objects.first()
        schedule.t_max = t_max
        schedule.t_necessary = t_necessary
        schedule.t_min = t_min
        schedule.save()
        return schedule

    def get_schedule(self):
        return ClimateSchedule.objects.first()

    def change_mod(self, mode: ClimateModeType):
        state = ClimateState.objects.first()
        state.mode = mode
        state.save()
        return state.mode

    def get_mode(self):
        return ClimateState.objects.first().mode

    def update_climate(self, work_type: WorkType):
        climate = Climate.objects.first()
        climate.work_type = work_type
        climate.save()
        return climate

    def get_climate(self):
        return Climate.objects.first()

    def init_values(self):
        if ClimateSchedule.objects.count() == 0:
            ClimateSchedule.objects.create(t_max=0, t_necessary=0, t_min=0)
        if Climate.objects.count() == 0:
            Climate.objects.create(work_type=WorkType.ventilation)
        if ClimateState.objects.count() == 0:
            ClimateState.objects.create(mode=ClimateModeType.off)
