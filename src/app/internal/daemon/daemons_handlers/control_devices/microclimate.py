import importlib.util
import time

try:
    import smbus
except ImportError:
    import app.pkg.fake_smbus
from decimal import Decimal

from app.internal.daemon.daemons_handlers.control_devices.PIN_settings import *
from app.internal.daemon.daemons_handlers.control_devices.servo import PCA9685, ServoPCA9685
from app.internal.rest.indicators.db.models import Temperature
from app.internal.rest.microclimate.db.models import ClimateState, ClimateSchedule, Climate, WorkType, ClimateModeType
from pydub import AudioSegment
from pydub.playback import play

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


class MicroclimateDaemon:
    def __init__(self):
        self.schedule: ClimateSchedule = None
        GPIO.setup(FAN_PIN, GPIO.OUT)
        GPIO.setup(HEAT_PIN, GPIO.OUT)
        GPIO.setup(DRIVE_PIN, GPIO.OUT)
        GPIO.output(DRIVE_PIN, GPIO.HIGH)
        i2cBus = smbus.SMBus(1)
        pca9685 = PCA9685.PCA9685(i2cBus)
        self.door_control = ServoPCA9685.ServoPCA9685(pca9685, PCA9685.CHANNEL00)
        self.heat_song = AudioSegment.from_mp3("src/sounds/нагрев.mp3")
        self.vent_song = AudioSegment.from_mp3("src/sounds/проветривание.mp3")
        self.sound_activated = False
        self.prev_state = WorkType.heat
        self.door_open = False

    def handle(self):
        while True:
            try:
                time.sleep(UPDATE_TIME)
                state = ClimateState.objects.first()
                if state is None:
                    continue
                elif state.mode == ClimateModeType.auto:
                    self._handle_auto_mode()
                elif state.mode == ClimateModeType.manual:
                    self._handle_manual_mode()
                else:
                    self.sound_activated = False
                    self._heat_off()
                    self._fan_off()
                    if self.door_open:
                        self._door_close()
                        self.door_open = False
            except Exception:
                pass

    def _handle_auto_mode(self):
        self._get_climate_schedule()

        if self.schedule is None:
            return

        current_temperature = self._get_current_temperature()
        if current_temperature > self.schedule.t_max:
            self._ventilation()
        elif current_temperature < self.schedule.t_min:
            self._heat()
        else:
            self.sound_activated = False
            self._heat_off()
            self._fan_off()
            if self.door_open:
                self._door_close()
                self.door_open = False

    def _get_climate_schedule(self):
        schedule = ClimateSchedule.objects.first()
        if schedule is not None:
            self.schedule = schedule

    def _heat(self):
        if not self.sound_activated:
            play(self.heat_song)
            self.sound_activated = True

        if not self.door_open:
            self._door_open()
            self.door_open = True
        self._fan_on()
        self._heat_on()
        while True:
            time.sleep(UPDATE_TIME)
            current_temperature = self._get_current_temperature()
            state = ClimateState.objects.first()
            if state.mode != ClimateModeType.auto:
                return
            if current_temperature >= self.schedule.t_necessary:
                self._heat_off()
                self._fan_off()
                if self.door_open:
                    self._door_close()
                    self.door_open = False
                return

    def _ventilation(self):
        if not self.sound_activated:
            play(self.vent_song)
            self.sound_activated = True
        if not self.door_open:
            self._door_open()
            self.door_open = True
        self._fan_on()
        while True:
            time.sleep(UPDATE_TIME)
            current_temperature = self._get_current_temperature()
            state = ClimateState.objects.first()
            if state.mode != ClimateModeType.auto:
                return
            if current_temperature <= self.schedule.t_necessary:
                self._heat_off()
                if self.door_open:
                    self._door_close()
                    self.door_open = False
                return

    def _handle_manual_mode(self):
        work_type = Climate.objects.first().work_type
        if work_type == WorkType.heat:
            if not self.sound_activated or self.prev_state == WorkType.ventilation:
                play(self.heat_song)
                self.sound_activated = True
                self.prev_state = WorkType.heat
            if not self.door_open:
                self._door_open()
                self.door_open = True
            self._fan_on()
            self._heat_on()
        else:
            if not self.sound_activated or self.prev_state == WorkType.heat:
                play(self.vent_song)
                self.sound_activated = True
                self.prev_state = WorkType.ventilation
            if not self.door_open:
                self._door_open()
                self.door_open = True
            self._fan_on()

    def _get_current_temperature(self):
        current_temperature = Temperature.objects.order_by("-time").first()
        current_temperature = Decimal(current_temperature.indication)
        return current_temperature

    def _fan_on(self):
        GPIO.output(FAN_PIN, GPIO.HIGH)

    def _fan_off(self):
        GPIO.output(FAN_PIN, GPIO.LOW)

    def _door_open(self):
        for angle in reversed(range(0, 90 + 1)):
            self.door_control.set_angle(angle)
            time.sleep(0.01)

    def _door_close(self):
        for angle in range(0, 90 + 1):
            self.door_control.set_angle(angle)
            time.sleep(0.01)

    def _heat_on(self):
        GPIO.output(HEAT_PIN, GPIO.HIGH)

    def _heat_off(self):
        GPIO.output(HEAT_PIN, GPIO.LOW)
