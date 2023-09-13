# Sensor Aggregator

Initial version of sensor aggregator codebase

## MVP goals

aggregate data across sensors into a database

Stretch Goals
- Viewable online
- incorporate MODIS vegetation data
- self healing nodes
- solar powered


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
Pannel: [Medium 6V 2W Solar Panel](https://www.adafruit.com/product/5366)\
Board (Charger): [Adafruit bq24074 Charger](https://www.adafruit.com/product/4755)\
battery: [Lithium Ion Battery 3.7v 2000mAh](https://www.adafruit.com/product/2011)\

### Satelite Imagery

greenery score
leverage sat data from [MODIS](https://lpdaac.usgs.gov/products/mod13a2v061/). use pixel color as a proxy for foliage density --> MODIS has an internal score they assign to each pixel


## Data store
On prem database with cloud backup. See [Database's documentation](Database/README.md)
#TODO: cloud option

## Wifi Mesh
In order to used meshing the wifi needs to support ()

All raspberry pi chips (newer) have it, but a cheaper 3rd party solution is somthing that should be considered.


## Resources
Relevant repo
https://github.com/binnes/WiFiMeshRaspberryPi/blob/master/part1/PIMESH.md

Source for Sat imagery
MODIS data provided by NASA

Source for historical temperature and rainfall


## Raspberry Pi Prep

It is probably best to [ssh](https://raspberrypi-guide.github.io/networking/connecting-via-ssh#:~:text=Enable%20SSH%20on%20the%20Raspberry%20Pi,-By%20default%2C%20SSH&text=To%20enable%20SSH%20via%20the,and%20enter%20sudo%20raspi%2Dconfig%20.) into the pi you are trying to update. 

### install circuit python
This enables the piboard to interact with its sensors. It takes a few steps to install.\
[How-to Guide](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/overview)\
[Helpful how-to video](https://www.youtube.com/watch?v=Epy6RvvpHOQ)


#TODO automate this via a script


# Future
Look into LoRa devices that are used for long range messaging.
could be a good low power alternative to the pi zero Ws being used now.

[performance testing different batman-adv algorithms](https://ieeexplore.ieee.org/document/8421863)


