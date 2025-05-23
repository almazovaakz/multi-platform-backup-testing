# DNS & DHCP Configuration Test

## Purpose
Verify network configuration on a virtual test machine.

## Steps
1. Run `ip a` to check assigned IP
2. Use `dig google.com` to test DNS
3. Ping external IP `ping 8.8.8.8`
4. View DHCP lease: `cat /var/lib/dhcp/dhclient.leases`

## Expected Results
Correct IP assigned, DNS resolution successful, lease file updated.
