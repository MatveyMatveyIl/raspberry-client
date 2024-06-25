import time
from subprocess import call
import base64
from threading import Thread

from app.internal.daemon.daemons_handlers.control_devices.PIN_settings import *
from app.internal.rest.camera.db.models import CameraImage


class CameraDaemon:
    def __init__(self):
        th = Thread(target=self._take_photo)
        th.start()

    def handle(self):
        while True:
            time.sleep(UPDATE_TIME)
            s_b64 = ""
            with open("src/app/internal/daemon/daemons_handlers/control_devices/camera/img.jpg", "rb") as img:
                s_b64 = base64.b64encode(img.read())
            cam = CameraImage.objects.first()
            cam.image_b64 = s_b64
            cam.save()
    
    def _take_photo(self):
        rc = call("src/app/internal/daemon/daemons_handlers/control_devices/camera/script.sh", shell=True)

