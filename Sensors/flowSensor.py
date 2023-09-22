

class flowSensor():
    SECONDS_IN_A_MINUTE = 60
    MS_IN_A_SECOND = 1000.0
    hertz = 0.0
    flow = 0  # in Liters per second
    thisFlow = 0.0  # in Liters
    totalFlow = 0.0  # in Liters

    def __init__(self,):
        self.hertz = 0.0
        self.flow = 0.0
        self.thisFlow = 0.0
        self.totalFlow = 0.0
        self.enabled = True

    def update(self, currentTime):
        # calculate the instantaneous speed
        if (self.enabled == True and self.clickDelta < 1000):
            self.hertz = flowSensor.MS_IN_A_SECOND / self.clickDelta
            self.flow = self.hertz / (flowSensor.SECONDS_IN_A_MINUTE * 7.5)  # In Liters per second
            instPour = self.flow * (self.clickDelta / flowSensor.MS_IN_A_SECOND)
            self.thisFlow += instPour
            self.totalFlow += instPour
        # Update the last click
        self.lastClick = currentTime

    def getFormattedHertz(self):
        return str(round(self.hertz, 3)) + ' Hz'

    def getFormattedFlow(self):
        return str(round(self.flow, 3)) + ' L/s'

    def getFormattedThisPour(self):
        return str(round(self.thisFlow, 3)) + ' L'

    def getFormattedTotalPour(self):
        return str(round(self.totalFlow, 3)) + ' L'

    def clear(self):
        self.thisFlow = 0
        self.totalFlow = 0