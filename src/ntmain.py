import logging
from src.frameworks_and_drivers.web_framework.flask_web_server import run_flask_server
from src.interface_adapters.packet_capture.scapy_packet_capture import start_packet_capture
from src.core.use_cases.detect_signatures import detect_attack_signatures
from src.core.use_cases.detect_anomalies import detect_network_anomalies
from src.core.use_cases.correlate_events import correlate_security_events
from src.frameworks_and_drivers.threat_intelligence.threat_data_api import fetch_threat_intelligence
from src.frameworks_and_drivers.machine_learning.anomaly_detection_model import AnomalyDetectionModel
from src.config.settings import Settings

# Configurações principais
settings = Settings()

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """
    Função principal que coordena as funcionalidades do NetWatch XDR.
    """
    logger.info("Iniciando o sistema NetWatch XDR...")

    # Carregar modelo de detecção de anomalias baseado em machine learning
    anomaly_model = AnomalyDetectionModel()
    anomaly_model.load_model(settings.anomaly_model_path)
    
    # Iniciar captura de pacotes de rede
    logger.info("Iniciando captura de pacotes de rede...")
    start_packet_capture(interface=settings.network_interface)
    
    # Iniciar detecção de assinaturas de ataques
    logger.info("Iniciando detecção de assinaturas de ataques...")
    detect_attack_signatures()

    # Detectar anomalias no tráfego de rede
    logger.info("Iniciando detecção de anomalias na rede...")
    detect_network_anomalies(anomaly_model)

    # Correlacionar eventos de segurança para insights mais profundos
    logger.info("Correlacionando eventos de segurança...")
    correlate_security_events()

    # Buscar inteligência de ameaças (Threat Intelligence) de fontes externas
    logger.info("Buscando dados de inteligência de ameaças...")
    threat_data = fetch_threat_intelligence()
    logger.info(f"Inteligência de ameaças recebida: {threat_data}")

    # Iniciar o dashboard web com Flask
    logger.info("Iniciando o servidor Flask para o dashboard web...")
    run_flask_server()

if __name__ == "__main__":
    main()
