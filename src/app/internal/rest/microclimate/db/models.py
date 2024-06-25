import uuid

from django.db import models
from django.db.models import TextChoices


class ClimateSchedule(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    t_max = models.DecimalField(verbose_name="Максимальная температура", max_digits=5, decimal_places=2)
    t_necessary = models.DecimalField(verbose_name="Необходимая температура", max_digits=5, decimal_places=2)
    t_min = models.DecimalField(verbose_name="Минимальная температура", max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Расписание микроклимата: temperature[{self.t_max}|{self.t_necessary}|{self.t_min}]"

    class Meta:
        verbose_name = "Schedule.Микроклимат"
        verbose_name_plural = "Schedule.Микроклимат"


class ClimateModeType(TextChoices):
    auto = 'авто'
    manual = 'ручной'
    off = 'выключено'


class ClimateState(models.Model):
    mode = models.CharField(choices=ClimateModeType.choices, verbose_name='тип работы')

    def __str__(self):
        return f"Состояние микроклимата: {self.mode}"

    class Meta:
        verbose_name = "State.Микроклимат"
        verbose_name_plural = "State.Микроклимат"


class WorkType(TextChoices):
    heat = 'Нагрев'
    ventilation = 'Проветривание'


class Climate(models.Model):
    work_type = models.CharField(choices=WorkType.choices, verbose_name='тип работы')

    def __str__(self):
        return f"Ручной микроклимат: {self.work_type}"

    class Meta:
        verbose_name = "Manual.Микроклимат"
        verbose_name_plural = "Manual.Микроклимат"
