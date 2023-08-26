CREATE TABLE VineLocations (
    VineNumber int NOT NULL,
    Coordinates ST_Point,
    PRIMARY KEY (VineNumber)
);