## WEP

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
