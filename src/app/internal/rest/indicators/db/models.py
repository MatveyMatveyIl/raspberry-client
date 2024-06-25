import uuid

from django.db import models


class Humidity(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    indication = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Влажность: [показание: {self.indication}, время: {self.time}]"

    class Meta:
        verbose_name = "ind.Влажность"
        verbose_name_plural = "ind.Влажность"


class HydrogenIndicator(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    indication = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"pH: [показание: {self.indication}, время: {self.time}]"

    class Meta:
        verbose_name = "ind.pH"
        verbose_name_plural = "ind.pH"


class Illumination(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    indication = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Освещение: [показание: {self.indication}, время: {self.time}]"

    class Meta:
        verbose_name = "ind.Освещение"
        verbose_name_plural = "ind.Освещение"


class SolutionConductivity(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    indication = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Проводимость раствора: [показание: {self.indication}, время: {self.time}]"

    class Meta:
        verbose_name = "ind.Проводимость раствора"
        verbose_name_plural = "ind.Проводимость раствора"


class Temperature(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    indication = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Температура: [показание: {self.indication}, время: {self.time}]"

    class Meta:
        verbose_name = "ind.Температура"
        verbose_name_plural = "ind.Температура"


class ReedSensor(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    indication = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Герконовый датчик: [показание: {self.indication}, время: {self.time}]"

    class Meta:
        verbose_name = "ind.Герконовый датчик"
        verbose_name_plural = "ind.Герконовый датчик"


class Soil(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, default=uuid.uuid4)
    indication = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Резистивный датчик влажности: [показание: {self.indication}, время: {self.time}]"

    class Meta:
        verbose_name = "ind.Резистивный датчик влажности"
        verbose_name_plural = "ind.Резистивный датчик влажности"