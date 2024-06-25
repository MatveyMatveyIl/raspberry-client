#!/bin/bash

fswebcam -q -r 640x480 --no-banner -S 20 --loop 5 src/app/internal/daemon/daemons_handlers/control_devices/camera/img.jpg >> /dev/null