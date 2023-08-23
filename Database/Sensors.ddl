CREATE TABLE SensorReadings (
    uUID text,
    hostID int,
    timestamp timestamp,
    sensorType varchar,
    lat geo,
    lon geo,
    soilMoisture FLOAT,
    sunlight FLOAT,
    temperature FLOAT,


)