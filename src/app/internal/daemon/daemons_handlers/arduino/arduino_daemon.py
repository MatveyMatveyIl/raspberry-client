import time
import serial
from serial.serialutil import SerialException
from datetime import datetime, timedelta

from app.internal.rest.indicators.db.models import *

class ArduinoDaemon():
    def __init__(self, port, baudrate, timeout, number):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.number = number
        self.indicator_name = None
        self.ser = None

    def handle(self):
        while True:
            if self.ser is None:
                try:
                    self._connect()
                except Exception:
                    time.sleep(2)
            else:
                try:
                    if not self.ser.is_open:
                        self._connect()

                    time.sleep(5)

                    if self.ser.in_waiting > 0:
                        value = self.ser.readline().decode("utf-8").strip()
                        self._save_indicator(value)
                except (SerialException, OSError):
                    print(f'[{self.number}] connection closed')
                    self.ser.close()
                    self.ser = None
                    time.sleep(2)

    def _connect(self):
        try:
            self.ser = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)
            time.sleep(3)
            self.ser.write("Who are you?".encode("utf-8"))
            time.sleep(1)
            self.indicator_name = self.ser.readline().decode("utf-8").strip()
            print(f'[{self.number}]{self.indicator_name} connected to {self.port}')
        except (SerialException, OSError):
            pass

    def _save_indicator(self, value):
        if self.indicator_name is None:
            return
        elif self.indicator_name == 'Humidity':
            Humidity.objects.create(indication=value)
            Humidity.objects.filter(time__lte=self._get_time_to_delete()).delete()
        elif self.indicator_name == 'HydrogenIndicator':
            HydrogenIndicator.objects.create(indication=value)
            HydrogenIndicator.objects.filter(time__lte=self._get_time_to_delete()).delete()
        elif self.indicator_name == 'Illumination':
            Illumination.objects.create(indication=value)
            Illumination.objects.filter(time__lte=self._get_time_to_delete()).delete()
        elif self.indicator_name == 'SolutionConductivity':
            SolutionConductivity.objects.create(indication=value)
            SolutionConductivity.objects.filter(time__lte=self._get_time_to_delete()).delete()
        elif self.indicator_name == 'Temperature':
            Temperature.objects.create(indication=value)
            Temperature.objects.filter(time__lte=self._get_time_to_delete()).delete()
        elif self.indicator_name == 'Soil':
            Soil.objects.create(indication=value)
            Soil.objects.filter(time__lte=self._get_time_to_delete()).delete()

    def _get_time_to_delete(self):
        return datetime.now() - timedelta(minutes=3)
