
import socket
import datetime
import sys
import time
import uuid
from statistics import mean
from pathlib import Path

# Necessary to import Database on nodes
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
print(sys.path)

from Database import dBUtils


import board #circut python package

from adafruit_seesaw.seesaw import Seesaw #circut python package

i2c_bus = board.I2C()  # uses board.SCL and board.SDA
# i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

ss = Seesaw(i2c_bus, addr=0x36) #determine address by looking at output of terminal command 'i2cdetect -y 1'

moistureReadings = []
tempReadings = []
while True:
    # collect 10 readings for an average
    while len(tempReadings) < 10:

        # read moisture level through capacitive touch pad
        moisture = ss.moisture_read()
        moistureReadings.append(moisture)
        # read temperature from the temperature sensor
        temp = ss.get_temp()
        tempReadings.append(temp)
        # print("temp: " + str(temp) + "  moisture: " + str(moisture))
        # sleep 5 se between readings
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
    # Sleep for 4 hrs between insertions
    time.sleep(14400)



