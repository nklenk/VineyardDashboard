# Portion of initial settup is one when creating the pi image.
# Including enabling ssh, setting wifi, etc.
# All can be later changed in the settings.

# Blinka install

# ssh into pi
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip

sudo pip3 install --upgrade setuptools


# Double check pi config and install Blinka
cd ~
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py

# Validate that folders were created
ls /dev/i2c* /dev/spi*

# Run blinkaTest.py to validate I2C and SPI connections are correct
python3 blinkaTest.py

# Now we can install required libraries
sudo pip3 install adafruit-circuitpython-seesaw # For the soil sensor

# Download circuit python image from https://circuitpython.org/downloads
# Be sure to select the correct board

# Download required libraries locally from (). Make sure they are the correct version

# scp circuit python libraries into the lib folder on the board

# ssh into pi
# Validate library files are accessible

# git clone repo

# run repo