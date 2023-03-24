from scapy.all import ARP, Ether, srp

target_ip = "192.168.1.73"

# create ARP packet
arp = ARP(pdst=target_ip)

# create the ether broadcast packet
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether/arp
result = srp(packet, timeout=3)[0]
clients = []

for sent, received in result:
    # for each response, append IP & MAC address
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))