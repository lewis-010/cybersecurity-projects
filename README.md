# Cybersecurity Projects

## Network Scanner
Network scanners are tools used to identify devices and systems connected to a network. They are essential in cybersecurity as they play a critical role in maintaining the overall health and security of a network. They help identify devices that are vulnerable to attack, detect rogue devices, and pinpoint potential security threats. Scanning a network also allows for the detection of unauthorized access and the identification of outdated or unpatched software that could leave a network open to attacks.

This Python program utlizes the Scapy library to create a network scanner. It scans a network for devices connected to it and returns their IP and MAC addresses. The code creates an ARP request and a broadcast Ethernet frame, sends them out to the network, captures the response, and prints out the IP and MAC addresses of each device that responded.
