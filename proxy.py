import os
import sys
import time

os.system('iptables -F;')
os.system('echo "FLUSHING IPTABLES!"')
os.system('iptables -t nat -F;')
os.system('echo "FLUSHING NAT"')
os.system('echo "1" > /proc/sys/net/ipv4/ip_forward;')
os.system('iptables -A FORWARD -i eth0 -j ACCEPT;')
os.system('iptables -A FORWARD -o eth0 -j ACCEPT;')
os.system('iptables -I FORWARD -i eth0 -p tcp --dport 1337 -j ACCEPT;')
os.system('echo "SETTING FAKE CNC PORT"')
os.system('iptables -t nat -A PREROUTING -p tcp --dport 1337 -j DNAT --to 1.1.1.1:80;')
os.system('echo "JUST LINKED THE CNC!"')
os.system('iptables -t nat -A POSTROUTING -j MASQUERADE;')
os.system('echo "Finished Setting PROXY!"')
