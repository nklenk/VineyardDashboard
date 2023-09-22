# SPDX-FileCopyrightText: 2019 Anne Barela for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# !/usr/bin/python
import time
import logging
import sys
import gpiozero as GPIO
from flowSensor import flowSensor

# boardRevision = GPIO.RPI_REVISION
GPIO.setmode(GPIO.BCM)  # use real GPIO numbering
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set up the flow meters
fm = flowSensor()

def doAClick(channel):
    currentTime = int(time.time() * flowSensor.MS_IN_A_SECOND)
    fm.update(currentTime)

GPIO.add_event_detect(16, GPIO.RISING, callback=doAClick, bouncetime=20)  # flow sensor on Pin 23

# main loop
while True:
    # Handle keyboard events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            GPIO.cleanup()
            fm.clear()

    currentTime = int(time.time() * flowSensor.MS_IN_A_SECOND)



    # Update db
