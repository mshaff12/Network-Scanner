from scapy.all import ARP, Ether, srp
import json
import socket

def scan_network(ip_range):
    # Create an ARP request packet
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)

    # Send the packet and capture responses
    result = srp(arp_request, timeout=3, verbose=0)[0]

    # Process the responses
    devices = []
    for sent, received in result:
        ip = received.psrc
        mac = received.hwsrc
        # password = input(f"Enter the password for device with IP {ip}: ")
        protocol = get_protocol(ip)
        name = get_device_name(ip)
        devices.append({'name':name, 'ip': ip, 'mac': mac, 'protocol': protocol})


    # Return the list of discovered devices
    return devices

def get_protocol(ip):
    # Perform a simple port-based protocol detection
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, 80))
            if result == 0:
                return 'HTTP'
            else:
                return 'HTTPS'
    except socket.error:
        return 'Unknown'

def get_device_name(ip):
    # Retrieve the device name using DNS resolution
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return 'Unknown'
    
# Define the IP range of your network
ip_range = "192.168.4.1/24"

# Scan the network and get the list of IoT devices
iot_devices = scan_network(ip_range)

# Print the discovered IoT devices
for device in iot_devices:
    print(f"IoT Device - Name: {device['name']}, IP: {device['ip']}, MAC: {device['mac']}, Prtocol: {device['protocol']}")

with open("iot_devices.json", "w") as f:
    json.dump(iot_devices, f)
