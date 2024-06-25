import importlib.util
import time
from datetime import datetime, timedelta

from app.internal.daemon.daemons_handlers.control_devices.PIN_settings import *
from app.internal.rest.light.db.models import LightSchedule, LightState, LightModeType, Light
from pydub import AudioSegment
from pydub.playback import play

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


class LightDaemon:
    def __init__(self):
        self.schedule: LightSchedule = None
        GPIO.setup(R_LIGHT_PIN, GPIO.OUT)
        GPIO.setup(G_LIGHT_PIN, GPIO.OUT)
        GPIO.setup(B_LIGHT_PIN, GPIO.OUT)
        self.r_light_control = GPIO.PWM(R_LIGHT_PIN, FREQUENCY)
        self.g_light_control = GPIO.PWM(G_LIGHT_PIN, FREQUENCY)
        self.b_light_control = GPIO.PWM(B_LIGHT_PIN, FREQUENCY)
        self.light_song = AudioSegment.from_mp3("src/sounds/свет.mp3")
        self.sound_activated = False

    def handle(self):
        while True:
            try:
                time.sleep(UPDATE_TIME)
                state = LightState.objects.first()
                if state is None:
                    continue
                elif state.mode == LightModeType.auto:
                    self._handle_auto_mode()
                elif state.mode == LightModeType.manual:
                    self._handle_manual_mode()
                else:
                    self._light_stop()
            except Exception:
                pass

    def _handle_auto_mode(self):
        self._get_light_schedule()

        if self.schedule is None:
            return

        time_now = (datetime.now() + timedelta(hours=5)).time()
        time_start = datetime.strptime(self.schedule.time_start, "%H:%M").time()
        time_end = datetime.strptime(self.schedule.time_end, "%H:%M").time()
        r_channel = self.schedule.R_channel
        g_channel = self.schedule.G_channel
        b_channel = self.schedule.B_channel

        if time_start <= time_now <= time_end:
            self._light_start(r_channel, g_channel, b_channel)
        else:
            self._light_stop()

    def _handle_manual_mode(self):
        light = Light.objects.first()
        self._light_start(light.R_channel, light.G_channel, light.B_channel)

    def _light_start(self, r_dc: int, g_dc: int, b_dc: int):
        if not self.sound_activated:
            play(self.light_song)
            self.sound_activated = True

        self.r_light_control.start(r_dc)
        self.g_light_control.start(g_dc)
        self.b_light_control.start(b_dc)

    def _light_stop(self):
        self.sound_activated = False
        self.r_light_control.stop()
        self.g_light_control.stop()
        self.b_light_control.stop()

    def _get_light_schedule(self):
        schedule = LightSchedule.objects.first()
        if schedule is not None:
            self.schedule = schedule
