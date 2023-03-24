import scapy.all as scapy

# Create a list of IP addresses to scan
ip_list = ['192.168.1.73']

# Iterate over each IP address in the list
for ip in ip_list:
    # Create an ARP request for the current IP address
    request = scapy.ARP() 
    request.pdst = ip + '/24'
    
    # Create a broadcast Ethernet frame
    broadcast = scapy.Ether() 
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    
    # Combine the ARP request and broadcast Ethernet frame
    request_broadcast = broadcast / request 
    
    # Send the packet and capture the response
    clients = scapy.srp(request_broadcast, timeout = 10,verbose = 1)[0] 
    
    # Print the IP and MAC addresses of each client that responded
    for element in clients: 
        print(element[1].psrc + "      " + element[1].hwsrc)
