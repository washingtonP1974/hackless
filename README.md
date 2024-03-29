# hackless
Pentesting wireless tricks

<div align="center">
<br/>
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXZiMm0zMGN3Nnlidm51aHBlMGw5NTE0YWw1YWNtazNxZmhsZmpodiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VOPK1BqsMEJRS/giphy.gif" alt="Gif">
</div>

Set of scripts in Python and bash, with the purpose of assisting wireless network testing, consider reading each readme.txt contained in each script folder.
Tuning each script to your settings.

# Scripts 

## Basic commands

- *monitor.sh* - Set monitor mode in a wireless interface

```
sh monitor.sh $INTERFACE
```

- *airodump.sh* - Set monitor mode and run Airodump in a wireless interface

```
sh airodump.sh $INTERFACE
```


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
```


# Frameworks

Script to download and install:
- wifiphisher
- wifijammer
- SniffAir
- WiFi-Pumpkin
- eaphammer


## Wep

- *wep_monitor.sh* - Set monitor mode and start monitoring networks 

```
sh wep_monitor.sh $INTERFACE $PCAP_NAME
```

- *wep_attack.sh* - Attack the network. Get around 100.000 IVs

```
sh wep_attack.sh $INTERFACE $AP_NAME $AP_MAC $CLIENT_MAC
```

- *wep_crack.sh* - Crack password from the pcap file

```
sh wep_crack.sh $PCAP_NAME
```


## Wpa

- *wpa_monitor.sh* - Set monitor mode and start monitoring networks 

```
sh wpa_monitor.sh $INTERFACE $PCAP_NAME
```

- *wpa_attack.sh* - Deauthenticate a client to get a 4-way handshake to crack

```
sh wpa_attack.sh $INTERFACE $AP_MAC $CLIENT_MAC
```

- *wpa_crack.sh* - Crack the pcap file using Aircrack-ng

```
sh wpa_crack.sh $PCAP_NAME
```

- *wpa_pyrit.sh* - Crack the pcap file using Pyrit

```
sh wpa_pyrit.sh $PCAP_NAME
```

- *pmkid_install.sh* - Install the needed dependencies for the PMKID attack

```
sh pmkid_install.sh
```

- *pmkid.sh* - Run the PMKID attack

```
sh pmkid.sh $MAC_ADDRESS $DICTIONARY
```

- *py_pmkid.py* - Run the PMKID attack

```
python py_pmkid.py [-h] [-f FILTER_FILE] [-p PCAP_FILE] [-j HASH_FILE] -d DICTIONARY -i MON_INTERFACE -m MAC_ADDRESS
```
