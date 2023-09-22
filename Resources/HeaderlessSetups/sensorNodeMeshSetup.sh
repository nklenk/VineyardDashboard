
# Sensor node settup
sudo apt-get install -y vim && sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install -y batctl

echo '#!/bin/bash
# batman-adv interface to use
sudo batctl if add wlan0
sudo ifconfig bat0 mtu 1468

# Tell batman-adv this is a gateway client
sudo batctl gw_mode client # gateway node is a server

# Activates batman-adv interfaces
sudo ifconfig wlan0 up
sudo ifconfig bat0 up
# Update x with an address from dnsmasq.conf. different for each node
sudo ifconfig bat0 192.168.199.x' >> ~/start-batman-adv.sh

chmod +x ~/start-batman-adv.sh

sudo touch /etc/network/interfaces.d/wlan0

#TODO: fix
sudo chmod 775 /etc/network/interfaces.d/wlan0

sudo echo 'auto wlan0
iface wlan0 inet manual
    mtu 1532 # Increase packet size to account for batman-adv header
    wireless-channel 1 # Any channel from 1-14
    wireless-essid call-code-mesh
    wireless-mode ad-hoc' >> /etc/network/interfaces.d/wlan0

echo 'batman-adv' | sudo tee --append /etc/modules

echo 'denyinterfaces wlan0' | sudo tee --append /etc/dhcpcd.conf  # if missed, node will connect to and mesh will form on home network

sudo vim /etc/rc.local
# insert before exit
$(pwd)/start-batman-adv.sh &

sudo shutdown -h now

/home/nklenk/start-batman-adv.sh &
