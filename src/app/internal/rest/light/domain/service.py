from app.internal.rest.light.db.models import LightSchedule, LightState, Light, LightModeType


class LightScheduleService:
    def update_light_schedule(self, R_channel: int, G_channel: int, B_channel: int, time_start: str, time_end: str):
        schedule = LightSchedule.objects.first()
        schedule.R_channel = R_channel
        schedule.G_channel = G_channel
        schedule.B_channel = B_channel
        schedule.time_start = time_start
        schedule.time_end = time_end
        schedule.save()
        return schedule

    def get_schedule(self):
        return LightSchedule.objects.first()

    def change_mod(self, mode: LightModeType):
        state = LightState.objects.first()
        state.mode = mode
        state.save()
        return state.mode

    def get_mode(self):
        return LightState.objects.first().mode

    def update_light(self, R_channel: int, G_channel: int, B_channel: int):
        light = Light.objects.first()
        light.R_channel = R_channel
        light.G_channel = G_channel
        light.B_channel = B_channel
        light.save()
        return light

    def get_light(self):
        return Light.objects.first()

    def init_values(self):
        if LightSchedule.objects.count() == 0:
            LightSchedule.objects.create(R_channel=0,
                                         G_channel=0,
                                         B_channel=0,
                                         time_start="00:00:00",
                                         time_end="00:00:00")
        if Light.objects.count() == 0:
            Light.objects.create(R_channel=0, G_channel=0, B_channel=0)
        if LightState.objects.count() == 0:
            LightState.objects.create(mode=LightModeType.off)
