## WPA

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
