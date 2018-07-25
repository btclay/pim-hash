# pim-hash

```
usage: pim_hash.py [-h] -g GROUP_ADDRESS -r RENDEZVOUS_POINT [-m MASK]

This will generate the calculate the PIM hash value for a Group, Mask, RP set
as defined in RFC7761.

optional arguments:
  -h, --help            show this help message and exit
  -g GROUP_ADDRESS, --group-address GROUP_ADDRESS
                        Multicast group address in question, in dotted decimal
                        format (eg, 239.0.0.1).
  -r RENDEZVOUS_POINT, --rendezvous-point RENDEZVOUS_POINT
                        IP address of the Rendezvous Point in question, in
                        dotted decimal format (eg, 10.0.1.2).
  -m MASK, --mask MASK  Group mask, in hexadecimal. Default value is
                        0xFFFFFFFC (CIDR equivalent /30) as defined in RFC
                        7761.
```
