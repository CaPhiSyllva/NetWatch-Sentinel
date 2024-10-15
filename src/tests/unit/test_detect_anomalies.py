import unittest
from src.core.use_cases.detect_anomalies import DetectAnomalies
from src.core.entities.network_traffic import NetworkTraffic

class TestDetectAnomalies(unittest.TestCase):

    def setUp(self):
        """Configurando o ambiente antes de cada teste."""
        self.detector = DetectAnomalies()
        # Exemplo de dados de tráfego de rede para teste
        self.sample_traffic = [
            NetworkTraffic(source_ip="192.168.1.1", dest_ip="192.168.1.2", protocol="TCP", size=1500),
            NetworkTraffic(source_ip="192.168.1.3", dest_ip="192.168.1.4", protocol="UDP", size=500),
            # Adicione mais dados de teste conforme necessário
        ]

    def test_anomaly_detection(self):
        """Testa a detecção de anomalias com um conjunto de dados."""
        anomalies = self.detector.detect(self.sample_traffic)
        # Verifica se o resultado contém as anomalias esperadas
        self.assertIsInstance(anomalies, list, "Deve retornar uma lista de anomalias.")
        # Adicione mais asserções baseadas nas anomalias esperadas
        self.assertGreater(len(anomalies), 0, "Deve haver anomalias detectadas.")

    def test_empty_traffic(self):
        """Testa a detecção de anomalias com dados de tráfego vazio."""
        anomalies = self.detector.detect([])
        self.assertEqual(anomalies, [], "Não deve haver anomalias detectadas em dados vazios.")

if __name__ == '__main__':
    unittest.main()
