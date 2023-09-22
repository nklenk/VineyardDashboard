# Portion of initial settup is one when creating the pi image.
# Including enabling ssh, setting wifi, etc.
# All can be later changed in the settings.

# Blinka install

# ssh into pi
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y python3-pip
sudo apt-get install -y git
sudo apt-get install -y libpq-dev

sudo pip3 install --upgrade setuptools
sudo pip3 install psycopg2

# Double check pi config and install Blinka
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py

# Validate that folders were created
ls /dev/i2c* /dev/spi*

# clone in the repo
git clone https://github.com/nklenk/VineyardDashboard.git
cd VineyardDashboard
git fetch

# Run blinkaTest.py to validate I2C and SPI connections are correct
python3 ~/VineyardDashboard/Resources/blinkaTest.py

# Now we can install required libraries
sudo pip3 install adafruit-circuitpython-seesaw # For the soil sensor


# Validate soil moisture sensor and attached temp sensor
python3 ~/VineyardDashboard/Sensors/soilMoistureInitTest.py

# the I2C connection needs to be expanded before any more sensors can be added


# Lux sensor
## install relevant library provided by Adafruit
## Adafruit circuitpython should already be installed
#sudo pip3 install adafruit-circuitpython-busdevice
#sudo pip3 install adafruit-circuitpython-tsl2591
#
## Validate lux and spectrums of sun sensor
#python3 ~/VineyardDashboard/Sensors/sunExposureInitTest.py