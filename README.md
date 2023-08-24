# Sensor Aggregator

Initial version of sensor aggregator codebase

## MVP goals

aggregate data across sensors into a database

Stretch Goals
- Viewable online
- self healing nodes
- solar powered
- Animal activity metric
- 

### Soil moisture 
Sensor Used:
[Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor - JST PH 2mm](https://www.adafruit.com/product/4026)

Considerations:
these values can be used as both a proxy to soil drainage as well as in aggregate to indicate overall water exposure


### Sun Exposure
Sensor Used:

Considerations:
some photo sensors are binary indicating that a threshold has been crossed
Sensors used are supposed to deliver a range of values 

### Temperature and Pressure
Sensor Used:

Considerations:


### Solar Power
Pannel:
Board:
battery:

### Satelite Imagery

greenery score
leverage sat data from [MODIS](https://lpdaac.usgs.gov/products/mod13a2v061/). use pixel color as a proxy for foliage density


## Data store
On prem database with cloud backup. See [Database's documentation](Database/README.md)

## Wifi Mesh
In order to used meshing the wifi needs to support ()

All raspberry pi chips (newer) have it, but a cheaper 3rd party solution is somthing that should be considered.


## Resources
Relevant repo
https://github.com/binnes/WiFiMeshRaspberryPi/blob/master/part1/PIMESH.md

Source for Sat imagery
MODIS data provided by NASA

Source for historical temperature and rainfall

Solar power considerations reference




