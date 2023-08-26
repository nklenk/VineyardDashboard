CREATE TABLE SensorReadings (
    UUID varchar(255) NOT NULL,
    Hostname int,
    Timestamp timestamp,
    SensorType varchar(255),
    SoilMoisture FLOAT,
    Sunlight FLOAT,
    Temperature FLOAT,
    PRIMARY KEY (UUID)
);