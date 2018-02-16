#!/bin/bash
sudo apt install openvpn
echo "Enter Username:"
stty -echo

read username
stty echo

echo "Enter Password:"
stty -echo

read pass
stty echo


wget https://vpn.iiit.ac.in/secure/ubuntu.ovpn --user=$username --password=$pass

sed -i 's/group.*/group nogroup/' ubuntu.ovpn 

sudo openvpn --config ubuntu.ovpn
