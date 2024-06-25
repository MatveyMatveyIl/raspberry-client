from django.db import models
from django_base64field.fields import Base64Field


class CameraImage(models.Model):
    image_b64 = Base64Field(max_length=900000, blank=True, null=True)

    def __str__(self):
        return f"{self.image_b64}"

    class Meta:
        verbose_name = "img"
        verbose_name_plural = "img"
