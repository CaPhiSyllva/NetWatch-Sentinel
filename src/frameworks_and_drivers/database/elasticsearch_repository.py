from elasticsearch import Elasticsearch, exceptions
from datetime import datetime

class ElasticSearchRepository:
    """
    Classe para gerenciar a interação com o Elasticsearch.
    """

    def __init__(self, host='localhost', port=9200):
        """
        Inicializa a conexão com o Elasticsearch.

        :param host: Endereço do host do Elasticsearch.
        :param port: Porta do Elasticsearch.
        """
        self.client = Elasticsearch([{'host': host, 'port': port}])
        self.index_name = 'network_events'

        # Verifica se o índice existe, caso contrário, cria um novo índice
        if not self.client.indices.exists(index=self.index_name):
            self.create_index()

    def create_index(self):
        """
        Cria um índice no Elasticsearch com a configuração apropriada.
        """
        mappings = {
            "mappings": {
                "properties": {
                    "timestamp": {"type": "date"},
                    "source_ip": {"type": "ip"},
                    "destination_ip": {"type": "ip"},
                    "protocol": {"type": "keyword"},
                    "alert_type": {"type": "keyword"},
                    "signature": {"type": "text"},
                    "severity": {"type": "keyword"},
                    "additional_info": {"type": "object"}
                }
            }
        }
        self.client.indices.create(index=self.index_name, body=mappings)
        print(f"Índice '{self.index_name}' criado com sucesso.")

    def store_event(self, event):
        """
        Armazena um evento no Elasticsearch.

        :param event: Dicionário contendo os dados do evento a serem armazenados.
        """
        try:
            event['timestamp'] = datetime.utcnow()  # Adiciona o timestamp atual
            self.client.index(index=self.index_name, body=event)
            print("Evento armazenado com sucesso.")
        except exceptions.ElasticsearchException as e:
            print(f"Erro ao armazenar evento: {e}")

    def get_events(self, query=None):
        """
        Recupera eventos do Elasticsearch.

        :param query: Dicionário contendo a consulta Elasticsearch.
        :return: Lista de eventos recuperados.
        """
        if query is None:
            query = {"query": {"match_all": {}}}  # Consulta padrão que retorna todos os eventos
        
        try:
            response = self.client.search(index=self.index_name, body=query)
            return [hit['_source'] for hit in response['hits']['hits']]
        except exceptions.ElasticsearchException as e:
            print(f"Erro ao recuperar eventos: {e}")
            return []

# Exemplo de uso
if __name__ == "__main__":
    # Inicializando o repositório Elasticsearch
    es_repo = ElasticSearchRepository()

    # Simulando um evento de tráfego para armazenar
    event_data = {
        "source_ip": "192.168.1.100",
        "destination_ip": "10.0.0.5",
        "protocol": "TCP",
        "alert_type": "Malicious Activity",
        "signature": "Suspicious Connection Attempt",
        "severity": "High",
        "additional_info": {
            "user_agent": "Mozilla/5.0",
            "geo_location": "US"
        }
    }

    # Armazenando o evento
    es_repo.store_event(event_data)

    # Recuperando e exibindo eventos
    retrieved_events = es_repo.get_events()
    print("Eventos recuperados:")
    for event in retrieved_events:
        print(event)
