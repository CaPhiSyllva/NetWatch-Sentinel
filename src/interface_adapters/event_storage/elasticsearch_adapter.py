from elasticsearch import Elasticsearch, exceptions
import logging
from settings import settings

# Configurando o logger
logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)

class ElasticsearchAdapter:
    def __init__(self):
        self.es = Elasticsearch(settings.elasticsearch_url)

    def index_document(self, index: str, doc_type: str, document: dict) -> dict:
        """Indexa um documento no Elasticsearch."""
        try:
            response = self.es.index(index=index, doc_type=doc_type, body=document)
            logger.info("Documento indexado com sucesso: %s", response)
            return response
        except exceptions.ElasticsearchException as e:
            logger.error("Erro ao indexar documento: %s", e)
            return {"error": str(e)}

    def search(self, index: str, query: dict) -> dict:
        """Realiza uma consulta no Elasticsearch."""
        try:
            response = self.es.search(index=index, body=query)
            logger.info("Consulta executada com sucesso: %s", response)
            return response
        except exceptions.ElasticsearchException as e:
            logger.error("Erro ao executar consulta: %s", e)
            return {"error": str(e)}

    def create_index(self, index: str, settings: dict = None) -> dict:
        """Cria um novo índice no Elasticsearch."""
        try:
            if not self.es.indices.exists(index):
                response = self.es.indices.create(index=index, body=settings)
                logger.info("Índice criado com sucesso: %s", response)
                return response
            else:
                logger.warning("Índice já existe: %s", index)
                return {"warning": "Índice já existe."}
        except exceptions.ElasticsearchException as e:
            logger.error("Erro ao criar índice: %s", e)
            return {"error": str(e)}

    def delete_index(self, index: str) -> dict:
        """Deleta um índice no Elasticsearch."""
        try:
            response = self.es.indices.delete(index=index)
            logger.info("Índice deletado com sucesso: %s", response)
            return response
        except exceptions.NotFoundError:
            logger.warning("Índice não encontrado para deletar: %s", index)
            return {"warning": "Índice não encontrado."}
        except exceptions.ElasticsearchException as e:
            logger.error("Erro ao deletar índice: %s", e)
            return {"error": str(e)}

# Exemplo de uso
if __name__ == "__main__":
    es_adapter = ElasticsearchAdapter()

    # Criar um índice
    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "timestamp": {"type": "date"},
                "message": {"type": "text"}
            }
        }
    }
    es_adapter.create_index("netwatch_xdr", index_settings)

    # Indexar um documento
    doc = {
        "timestamp": "2024-10-15T12:00:00",
        "message": "Teste de indexação no Elasticsearch."
    }
    es_adapter.index_document("netwatch_xdr", "_doc", doc)

    # Realizar uma consulta
    query = {
        "query": {
            "match_all": {}
        }
    }
    search_results = es_adapter.search("netwatch_xdr", query)
    print("Resultados da pesquisa:", search_results)
