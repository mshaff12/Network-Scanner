from flask import Flask, jsonify, request
from scanner import scan_network, perform_vulnerability_assessment

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan_network_endpoint():
    # Perform network scanning
    ip_range = request.json['ip_range']
    devices = scan_network(ip_range)

    # Return the list of discovered devices
    return jsonify({'devices': devices})

@app.route('/assess', methods=['POST'])
def assess_device_endpoint():
    # Perform vulnerability assessment for a device
    device = request.json['device']
    vulnerabilities = perform_vulnerability_assessment(device)

    # Return the list of vulnerabilities
    return jsonify({'vulnerabilities': vulnerabilities})

if __name__ == '__main__':
    app.run(debug=True)
