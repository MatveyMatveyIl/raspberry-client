import importlib.util
import time
from datetime import datetime, timedelta

from app.internal.daemon.daemons_handlers.control_devices.PIN_settings import *
from app.internal.rest.indicators.db.models import ReedSensor

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


class ReedSensorDaemon:
    def __init__(self):
        GPIO.setup(REED_PIN_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(REED_PIN_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def handle(self):
        while True:
            try:
                time.sleep(UPDATE_TIME)
                state = GPIO.input(REED_PIN_DOWN)
                if state == 0:
                    ReedSensor.objects.create(indication="Пустой")
                else:
                    ReedSensor.objects.create(indication="Полный")

                ReedSensor.objects.filter(time__lte=self.get_time_to_delete()).delete()
            except Exception:
                pass

    def get_time_to_delete(self):
        return datetime.now() - timedelta(minutes=2)
