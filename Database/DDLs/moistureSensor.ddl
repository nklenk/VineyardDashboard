CREATE TABLE MoistureSensorReadings (
    UUID varchar(255) NOT NULL,
    Hostname varchar(255),
    Timestamp timestamp,
    SoilMoisture FLOAT,
    Temperature FLOAT,
    PRIMARY KEY (UUID)
);