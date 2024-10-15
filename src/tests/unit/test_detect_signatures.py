import unittest
from src.core.use_cases.detect_signatures import DetectSignatures
from src.core.entities.network_traffic import NetworkTraffic

class TestDetectSignatures(unittest.TestCase):

    def setUp(self):
        """Configurando o ambiente antes de cada teste."""
        self.signatures_detector = DetectSignatures()
        # Exemplo de dados de tráfego de rede para teste
        self.sample_traffic = [
            NetworkTraffic(source_ip="192.168.1.1", dest_ip="192.168.1.2", protocol="TCP", size=1500, payload="malicious payload"),
            NetworkTraffic(source_ip="192.168.1.3", dest_ip="192.168.1.4", protocol="UDP", size=500, payload="normal payload"),
            # Adicione mais dados de teste conforme necessário
        ]
        
        # Assinaturas de exemplo
        self.signatures = [
            {"signature": "malicious payload", "description": "Malware signature"},
            {"signature": "suspicious behavior", "description": "Suspicious activity"},
            # Adicione mais assinaturas conforme necessário
        ]

    def test_signature_detection(self):
        """Testa a detecção de assinaturas com um conjunto de dados."""
        detections = self.signatures_detector.detect(self.sample_traffic, self.signatures)
        # Verifica se o resultado contém as detecções esperadas
        self.assertIsInstance(detections, list, "Deve retornar uma lista de detecções.")
        self.assertGreater(len(detections), 0, "Deve haver assinaturas detectadas.")

    def test_no_signatures_detected(self):
        """Testa a detecção de assinaturas sem encontrar nenhuma."""
        clean_traffic = [
            NetworkTraffic(source_ip="192.168.1.5", dest_ip="192.168.1.6", protocol="TCP", size=1500, payload="innocuous payload"),
        ]
        detections = self.signatures_detector.detect(clean_traffic, self.signatures)
        self.assertEqual(detections, [], "Não deve haver assinaturas detectadas em tráfego limpo.")

if __name__ == '__main__':
    unittest.main()
