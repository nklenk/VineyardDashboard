CREATE TABLE MoistureSensorReadings (
    UUID varchar(255) NOT NULL,
    Timestamp timestamp,
    SoilMoisture FLOAT,
    Temperature FLOAT,
    PRIMARY KEY (UUID)
);