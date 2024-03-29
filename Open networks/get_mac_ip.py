import sys
import argparse as arg
import nmap

parser = arg.ArgumentParser()
parser.add_argument("-i", "--interface", help="Interface", required=True)
parser.add_argument("-a", "--address", help="IP address", required=True)
argument = parser.parse_args()


def scan_mac(ip, iface='wlan0'):
        dict_ = []
        scan = nmap.PortScanner().scan(hosts=ip + '/24',arguments='-sP '+ iface, sudo=True).get('scan')
        for i in scan.keys():
                mac = scan.get(scan.keys()[scan.keys().index(i)]).get('addresses').get('mac')
                dict_.append({'ip':i, 'mac':mac})
        return dict_


def main():
        res = scan_mac(argument.address, argument.interface)
        for j in sorted(res, key = lambda i: i['ip']):
                print j


main()              
