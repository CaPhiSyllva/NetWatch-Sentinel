import requests

class ThreatIntelligence:
    """
    Classe para gerenciar a inteligência de ameaças.
    """

    def __init__(self):
        self.sources = [
            "https://api.threatintel.com/v1/feeds",
            "https://api.anotherthreatsource.com/threats"
            # Adicione mais fontes de inteligência conforme necessário
        ]

    def fetch_threat_data(self):
        """
        Busca dados de inteligência de ameaças de várias fontes.

        :return: Lista de dados de inteligência de ameaças.
        """
        threat_data = []
        for source in self.sources:
            try:
                response = requests.get(source)
                response.raise_for_status()
                data = response.json()
                threat_data.extend(data.get("threats", []))
            except requests.RequestException as e:
                print(f"Erro ao buscar dados da fonte {source}: {e}")
        return threat_data

    def process_threat_data(self, raw_data):
        """
        Processa os dados de inteligência de ameaças.

        :param raw_data: Dados brutos de inteligência de ameaças.
        :return: Lista de ameaças processadas.
        """
        processed_threats = []
        for item in raw_data:
            threat = {
                "id": item.get("id"),
                "name": item.get("name"),
                "description": item.get("description"),
                "type": item.get("type"),
                "severity": item.get("severity"),
                "timestamp": item.get("timestamp")
            }
            processed_threats.append(threat)
        return processed_threats

    def enrich_alerts_with_threat_data(self, alerts, threat_data):
        """
        Enriquecer alertas com dados de inteligência de ameaças.

        :param alerts: Lista de alertas a serem enriquecidos.
        :param threat_data: Dados de inteligência de ameaças.
        :return: Lista de alertas enriquecidas.
        """
        for alert in alerts:
            for threat in threat_data:
                if alert["signature"] == threat["name"]:
                    alert["threat_info"] = {
                        "id": threat["id"],
                        "description": threat["description"],
                        "severity": threat["severity"]
                    }
        return alerts

# Exemplo de uso
if __name__ == "__main__":
    # Inicializando a classe de inteligência de ameaças
    threat_intel = ThreatIntelligence()

    # Buscando dados de inteligência de ameaças
    raw_threat_data = threat_intel.fetch_threat_data()

    # Processando os dados de ameaças
    processed_threats = threat_intel.process_threat_data(raw_threat_data)

    # Simulando algumas alertas para enriquecer
    alerts = [
        {"signature": "Malicious File Download", "timestamp": "2024-10-15T12:00:00Z"},
        {"signature": "Phishing Attempt", "timestamp": "2024-10-15T12:05:00Z"}
    ]

    # Enriquecendo as alertas com dados de inteligência de ameaças
    enriched_alerts = threat_intel.enrich_alerts_with_threat_data(alerts, processed_threats)

    # Exibindo os alertas enriquecidos
    for alert in enriched_alerts:
        print(alert)
