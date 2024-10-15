import os

class Settings:
    def __init__(self):
        # Configurações de Rede
        self.network_interface = os.getenv('NETWORK_INTERFACE', 'any')  # Interface 'any' captura todas as interfaces de rede
        self.packet_capture_filter = os.getenv('PACKET_CAPTURE_FILTER', 'tcp or udp or icmp or arp')  # Filtros para captura de todos os tipos de pacotes
        
        # Caminhos dos modelos de ML
        self.anomaly_model_path = os.getenv('ANOMALY_MODEL_PATH', 'models/anomaly_detection_model.pkl')
        
        # Configurações de integração
        self.threat_intelligence_api_key = os.getenv('THREAT_INTELLIGENCE_API_KEY', 'your-api-key')
        self.elasticsearch_url = os.getenv('ELASTICSEARCH_URL', 'http://localhost:9200')
        self.mysql_db_url = os.getenv('MYSQL_DB_URL', 'mysql://user:password@localhost/netwatch_xdr')  # Descomentado para uso
        
        # Configurações de segurança
        self.enable_firewall_integration = os.getenv('ENABLE_FIREWALL_INTEGRATION', 'true').lower() == 'true'
        
        # Configurações do Flask
        self.flask_host = os.getenv('FLASK_HOST', '0.0.0.0')
        self.flask_port = int(os.getenv('FLASK_PORT', 5000))
        
        # Configurações de logging
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')
        
        # Outras configurações
        self.environment = os.getenv('ENVIRONMENT', 'development')  # Alternar entre 'development', 'testing' e 'production'
        self.auto_update_signatures = os.getenv('AUTO_UPDATE_SIGNATURES', 'true').lower() == 'true'
        
    def get_database_config(self):
        return {
            "url": self.mysql_db_url,  # Retorna a URL do banco de dados MySQL
        }
    
    def get_elasticsearch_config(self):
        return {
            "url": self.elasticsearch_url,  # Retorna a URL do Elasticsearch
        }
    
    def get_logging_config(self):
        return {
            "level": self.log_level
        }

# Instância global das configurações
settings = Settings()
