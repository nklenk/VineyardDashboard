CREATE TABLE HostLocations (
    Hostname varchar(255) NOT NULL,
    Coordinates ST_Point,
    PRIMARY KEY (Hostname)
);