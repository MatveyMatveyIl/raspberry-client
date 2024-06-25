import importlib.util
import json
import time
from threading import Thread

import serial

from app.internal.daemon.daemons_handlers.arduino.arduino_daemon import ArduinoDaemon
from app.internal.daemon.daemons_handlers.control_devices.camera.camera import CameraDaemon
from app.internal.daemon.daemons_handlers.control_devices.irrigation import IrrigationDaemon
from app.internal.daemon.daemons_handlers.control_devices.light import LightDaemon
from app.internal.daemon.daemons_handlers.control_devices.microclimate import MicroclimateDaemon
from app.internal.daemon.daemons_handlers.control_devices.reed_sensor import ReedSensorDaemon
from app.internal.daemon.daemons_handlers.control_devices.screen import ScreenDaemon

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


class Daemons:
    def __init__(self):
        self.ports_prefix = "/dev/ttyUSB"

    def start_daemons(self):
        try:
            print('Start daemons')
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            threads = []

            for i in range(10):
                daemon = ArduinoDaemon(f'{self.ports_prefix}{i}', 9600, 5, i)
                th = Thread(target=daemon.handle)
                threads.append(th)
            
            daemon = LightDaemon()
            th = Thread(target=daemon.handle)
            threads.append(th)

            daemon = IrrigationDaemon()
            th = Thread(target=daemon.handle)
            threads.append(th)

            daemon = MicroclimateDaemon()
            th = Thread(target=daemon.handle)
            threads.append(th)

            daemon = ReedSensorDaemon()
            th = Thread(target=daemon.handle)
            threads.append(th)

            daemon = ScreenDaemon()
            th = Thread(target=daemon.handle)
            threads.append(th)
   
            daemon = CameraDaemon()
            th = Thread(target=daemon.handle)
            threads.append(th)

            for thread in threads:
                thread.start()
        except KeyboardInterrupt:
            GPIO.cleanup()
