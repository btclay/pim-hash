#!/usr/bin/env python3

import argparse
import sys
from ipaddress import ip_address

class ArgParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def pim_hash(group, mask, crp):
    # All values should be type int
    #Value(G,M,C(i))= (1103515245 * ((1103515245 * (G&M)+12345) XOR C(i)) + 12345) mod 2^31

    value = (1103515245 * ((1103515245 * (group & mask) + 12345) ^ crp) + 12345) % 2**31

    return value

def main():
    parser = ArgParser(prog = 'pim_hash.py',
                       description = 'This will generate the calculate the PIM hash value for a Group, Mask, RP set as defined in RFC7761.')
    
    parser.add_argument('-g', '--group-address',
                        dest = 'group_address',
                        help = 'Multicast group address in question, in dotted decimal format (eg, 239.0.0.1).',
                        type = str,
                        required = True)

    parser.add_argument('-r', '--rendezvous-point',
                        dest = 'rendezvous_point',
                        help = 'IP address of the Rendezvous Point in question, in dotted decimal format (eg, 10.0.1.2).',
                        type = str,
                        required = True)

    parser.add_argument('-m', '--mask',
                        dest = 'mask',
                        help = 'Group mask, in hexadecimal. Default value is 0xFFFFFFFC (CIDR equivalent /30) as defined in RFC 7761.',
                        type = str,
                        default = '0xFFFFFFFC')

    args = parser.parse_args()

    gaddr = ip_address(args.group_address)

    crp = ip_address(args.rendezvous_point)

    mask = args.mask

    hash = pim_hash(int(gaddr), int(mask, 16), int(crp))

    print(hash)

    
main()