#!/sh

IFACE='wlan0'
airmon-ng check kill
ifconfig $IFACE down
iwconfig $IFACE mode monitor
ifconfig $IFACE up
airodump-ng $IFACE -w $2
