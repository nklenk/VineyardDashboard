CREATE TABLE FoliageScore (
    UUID varchar(255) NOT NULL,
    Timestamp timestamp,
    PixelValuesR int,
    PixelValuesG int,
    PixelValuesB int,
    BBOX ST_Polygon,
    PRIMARY KEY (UUID)
);