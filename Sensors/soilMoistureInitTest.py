# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import uuid
from Database import dBUtils
import socket
import datetime
from statistics import mean

import board #circut python package

from adafruit_seesaw.seesaw import Seesaw #circut python package

i2c_bus = board.I2C()  # uses board.SCL and board.SDA
# i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

ss = Seesaw(i2c_bus, addr=0x36) #determine address by looking at output of terminal command 'i2cdetect -y 1'

moistureReadings = []
tempReadings = []
while len(tempReadings) < 10:

    # read moisture level through capacitive touch pad
    moisture = ss.moisture_read()
    moistureReadings.append(moisture)
    # read temperature from the temperature sensor
    temp = ss.get_temp()
    tempReadings.append(temp)
    print("temp: " + str(temp) + "  moisture: " + str(moisture))
    time.sleep(5)



# Send to the table
insertTemp = round(mean(tempReadings), 3)
print("insertTemp: {}".format(insertTemp))
insertMoisture = round(mean(moistureReadings), 3)
print("insertMoisture: {}".format(insertMoisture))
db = dBUtils.DBUtils()
currentUuid = str(uuid.uuid4())
hostname = socket.gethostname()
currentTimestamp = datetime.datetime.now()
insertQuery = "INSERT INTO moisturesensorreadings (UUID, HOSTNAME, TIMESTAMP, SOILMOISTURE, TEMPERATURE) VALUES ({}, {}, {}, {}, {})".format("'"+currentUuid+"'", "'"+hostname+"'", "'"+str(currentTimestamp)+"'", moisture, temp)
print("insertQuery: {}".format(insertQuery))
db.execute(insertQuery)



