from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Mock data for demonstration
mock_data = {
    "packet_capture": {
        "status": "Running",
        "packets_captured": 1520,
        "last_capture_time": "2024-10-15 14:32:45"
    },
    "firewall_rules": [
        {"id": 1, "rule": "ALLOW tcp from any to any port 80", "status": "Active"},
        {"id": 2, "rule": "DENY all from 192.168.1.100", "status": "Active"},
        {"id": 3, "rule": "ALLOW udp from any to any port 53", "status": "Inactive"},
    ],
    "threat_intelligence": {
        "latest_alerts": [
            {"source": "VirusTotal", "threat": "Malware detected", "time": "2024-10-15 13:45:00"},
            {"source": "AlienVault OTX", "threat": "DDoS attack detected", "time": "2024-10-15 12:30:00"},
        ]
    }
}

@app.route('/')
def index():
    return render_template('dashboard.html', data=mock_data)

@app.route('/api/status')
def status():
    return jsonify(mock_data)

if __name__ == '__main__':
    # Configurações do Flask
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    
    app.run(host=host, port=port)
