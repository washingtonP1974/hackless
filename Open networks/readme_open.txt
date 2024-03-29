## Open networks

- *change_mac_ip.py* - Scan the IP and MAC addresses of your network and change to those IP and MAC addresses -

```
python change_mac_ip.py [-h] -a ADDRESS -i INTERFACE
```

- *change_mac_ip.sh* - Change IP and MAC address of an interface to specific values

```
sh change_mac_ip.sh $INTERFACE $IP_ADDRESS $GATEWAY $MAC_ADRESS
```

- *get_mac_ip.py* - List IP and MAC addresses of devices in your network

```
python get_mac_ip.py [-h] -i INTERFACE -a ADDRESS
```

- *get_mac_ip.sh* - List IP and MAC addresses of devices in your network

```
sh get_mac_ip.sh $NETWORK
```

Example: *sh get_mac_ip.sh 192.168.79.0/24*


- *iodine_server.sh* - Start Iodine server

```
sh iodine_server.sh $PASSWORD $DNS_SERVER_IP $DOMAIN
```

- *iodine_client.sh* - Connect to Iodine server

```
sh iodine_client.sh $PASSWORD $DNS_SERVER_IP $DOMAIN
```

- *start_ettercap.sh* - Run ettercap in graphical mode

```
sh start_ettercap.sh
```

- *start_wireshark.sh* - Run wireshark

```
sh start_wireshark.sh
