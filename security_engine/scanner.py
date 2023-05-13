from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    # Create an ARP request packet
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)

    # Send the packet and capture responses
    result = srp(arp_request, timeout=3, verbose=0)[0]

    # Process the responses
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    # Return the list of discovered devices
    return devices

# Define the IP range of your network
ip_range = "192.168.4.1/24"

# Scan the network and get the list of IoT devices
iot_devices = scan_network(ip_range)

# Print the discovered IoT devices
for device in iot_devices:
    print(f"IoT Device - IP: {device['ip']}, MAC: {device['mac']}")
