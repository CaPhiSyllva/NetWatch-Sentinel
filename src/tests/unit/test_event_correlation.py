import unittest
from src.core.use_cases.correlate_events import CorrelateEvents
from src.core.entities.network_event import NetworkEvent

class TestEventCorrelation(unittest.TestCase):

    def setUp(self):
        """Configurando o ambiente antes de cada teste."""
        self.event_correlation = CorrelateEvents()
        # Exemplo de eventos de rede para teste
        self.sample_events = [
            NetworkEvent(timestamp="2024-10-15T10:00:00Z", source_ip="192.168.1.1", dest_ip="192.168.1.2", event_type="login_attempt", status="failed"),
            NetworkEvent(timestamp="2024-10-15T10:01:00Z", source_ip="192.168.1.1", dest_ip="192.168.1.2", event_type="login_attempt", status="successful"),
            NetworkEvent(timestamp="2024-10-15T10:02:00Z", source_ip="192.168.1.3", dest_ip="192.168.1.4", event_type="file_access", status="success"),
            # Adicione mais eventos de teste conforme necessário
        ]
        
    def test_correlation_of_events(self):
        """Testa a correlação de eventos baseando-se em padrões definidos."""
        correlated_events = self.event_correlation.correlate(self.sample_events)
        # Verifica se o resultado contém as correlações esperadas
        self.assertIsInstance(correlated_events, list, "Deve retornar uma lista de eventos correlacionados.")
        self.assertGreater(len(correlated_events), 0, "Deve haver eventos correlacionados.")

    def test_no_correlation_found(self):
        """Testa a correlação de eventos sem encontrar correlações."""
        unrelated_events = [
            NetworkEvent(timestamp="2024-10-15T11:00:00Z", source_ip="192.168.2.1", dest_ip="192.168.2.2", event_type="login_attempt", status="successful"),
            NetworkEvent(timestamp="2024-10-15T11:01:00Z", source_ip="192.168.2.3", dest_ip="192.168.2.4", event_type="file_access", status="success"),
        ]
        correlated_events = self.event_correlation.correlate(unrelated_events)
        self.assertEqual(correlated_events, [], "Não deve haver eventos correlacionados entre eventos não relacionados.")

if __name__ == '__main__':
    unittest.main()
