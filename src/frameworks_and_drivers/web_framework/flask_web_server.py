from flask import Flask, jsonify, request
from settings import settings
from core.entities.network_traffic import NetworkTraffic
from core.use_cases.detect_signatures import DetectSignatures
from core.use_cases.detect_anomalies import DetectAnomalies
from core.use_cases.correlate_events import CorrelateEvents
from core.use_cases.respond_to_incidents import RespondToIncidents
from core.use_cases.update_signatures import UpdateSignatures

app = Flask(__name__)

# Configurações do Flask
app.config['HOST'] = settings.flask_host
app.config['PORT'] = settings.flask_port
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def home():
    return jsonify({"message": "Bem-vindo ao NetWatch XDR!"})

@app.route('/api/network_traffic', methods=['POST'])
def capture_network_traffic():
    data = request.json
    traffic = NetworkTraffic(data['source'], data['destination'], data['protocol'], data['timestamp'])
    # Aqui você chamaria a função para capturar pacotes
    return jsonify({"message": "Captura de tráfego iniciada.", "traffic": traffic.__dict__}), 200

@app.route('/api/detect_signatures', methods=['POST'])
def detect_signatures():
    detector = DetectSignatures()
    results = detector.run()  # Método que executa a detecção
    return jsonify({"results": results}), 200

@app.route('/api/detect_anomalies', methods=['POST'])
def detect_anomalies():
    detector = DetectAnomalies()
    results = detector.run()  # Método que executa a detecção de anomalias
    return jsonify({"results": results}), 200

@app.route('/api/correlate_events', methods=['POST'])
def correlate_events():
    correlator = CorrelateEvents()
    results = correlator.run()  # Método que executa a correlação de eventos
    return jsonify({"results": results}), 200

@app.route('/api/respond_to_incidents', methods=['POST'])
def respond_to_incidents():
    responder = RespondToIncidents()
    response = responder.run()  # Método que executa a resposta a incidentes
    return jsonify({"message": "Resposta ao incidente executada.", "response": response}), 200

@app.route('/api/update_signatures', methods=['POST'])
def update_signatures():
    updater = UpdateSignatures()
    updater.run()  # Método que executa a atualização de assinaturas
    return jsonify({"message": "Assinaturas atualizadas com sucesso."}), 200

if __name__ == '__main__':
    app.run(host=settings.flask_host, port=settings.flask_port)
