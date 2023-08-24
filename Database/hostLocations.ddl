CREATE TABLE HostLocations (
    Hostname varchar(255) NOT NULL,
    Lat geo,
    Lon geo,
    PRIMARY KEY (Hostname)
)