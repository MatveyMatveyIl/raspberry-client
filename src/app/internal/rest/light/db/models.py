import uuid

from django.db import models
from django.db.models import TextChoices


class LightSchedule(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    R_channel = models.IntegerField(verbose_name="красный канал")
    G_channel = models.IntegerField(verbose_name="зеленый канал")
    B_channel = models.IntegerField(verbose_name="синий канал")
    time_start = models.CharField(verbose_name="начало расписания")
    time_end = models.CharField(verbose_name="конец расписания")

    def __str__(self):
        return f"Расписание освещения: {self.time_start}|{self.time_end}"

    class Meta:
        verbose_name = "Schedule.Освещение"
        verbose_name_plural = "Schedule.Освещение"


class LightModeType(TextChoices):
    auto = 'авто'
    manual = 'ручной'
    off = 'выключено'


class LightState(models.Model):
    mode = models.CharField(choices=LightModeType.choices, verbose_name='тип работы')

    def __str__(self):
        return f"Состояние освещения: {self.mode}"

    class Meta:
        verbose_name = "State.Освещение"
        verbose_name_plural = "State.Освещение"


class Light(models.Model):
    R_channel = models.IntegerField(verbose_name="красный канал")
    G_channel = models.IntegerField(verbose_name="зеленый канал")
    B_channel = models.IntegerField(verbose_name="синий канал")

    def __str__(self):
        return f"Ручное освещение {self.R_channel}-{self.G_channel}-{self.B_channel}"

    class Meta:
        verbose_name = "Manual.Освещение"
        verbose_name_plural = "Manual.Освещение"
