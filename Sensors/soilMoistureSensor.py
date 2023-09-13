
import time

import board #circut python package

from adafruit_seesaw.seesaw import Seesaw #circut python package

class SoilMoisture:
        def __init__(self, sensorAddress): # 0x36
            """
            :type sensorAddress: object
            """
            self.sensorAddress = sensorAddress
            self.sensorConnection = self.connectToMoistureSensor()

        def connectToMoistureSensor(self):
            i2c_bus = board.I2C()
            ss = Seesaw(i2c_bus, addr=0x36)

            return ss
        def retrieveSoilMoistureValue(self):
            return self.sensorConnection.moisture_read()

        def retrieveSensorTemp(self):
            return self.sensorConnection.get_temp()
