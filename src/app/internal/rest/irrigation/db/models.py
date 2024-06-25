import uuid

from django.db import models
from django.db.models import TextChoices


class IrrigationSchedule(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    time_start = models.CharField(verbose_name="начало расписания")
    duration = models.DecimalField(verbose_name="продолжительность", max_digits=5, decimal_places=2)
    power = models.IntegerField(verbose_name="мощность")

    def __str__(self):
        return f"Расписание полива: [{self.time_start}|{self.duration}|{self.power}]"

    class Meta:
        verbose_name = "Schedule.Полив"
        verbose_name_plural = "Schedule.Полив"


class IrrigationModeType(TextChoices):
    auto = 'авто'
    manual = 'ручной'
    off = 'выключено'


class IrrigationState(models.Model):
    mode = models.CharField(choices=IrrigationModeType.choices, verbose_name='тип работы')

    def __str__(self):
        return f"Состояние полива: {self.mode}"

    class Meta:
        verbose_name = "State.Полив"
        verbose_name_plural = "State.Полив"


class Irrigation(models.Model):
    power = models.IntegerField(verbose_name="мощность")

    def __str__(self):
        return f"Ручной полив: {self.power}"

    class Meta:
        verbose_name = "Manual.Полив"
        verbose_name_plural = "Manual.Полив"
