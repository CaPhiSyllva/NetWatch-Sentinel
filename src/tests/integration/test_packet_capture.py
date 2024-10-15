import unittest
from scapy.all import *
from scapy_packet_capture import PacketCapture  # Certifique-se de que o caminho para PacketCapture esteja correto

class TestPacketCapture(unittest.TestCase):

    def setUp(self):
        """Configuração inicial antes de cada teste."""
        self.packet_capture = PacketCapture()

    def test_start_capture(self):
        """Teste para iniciar a captura de pacotes."""
        result = self.packet_capture.start_capture()
        self.assertTrue(result)  # Verifica se a captura foi iniciada com sucesso

    def test_stop_capture(self):
        """Teste para parar a captura de pacotes."""
        self.packet_capture.start_capture()  # Inicia a captura primeiro
        result = self.packet_capture.stop_capture()
        self.assertTrue(result)  # Verifica se a captura foi parada com sucesso

    def test_packet_filter(self):
        """Teste para verificar se o filtro de pacotes está funcionando."""
        self.packet_capture.set_filter('tcp')  # Define um filtro de exemplo
        current_filter = self.packet_capture.get_filter()
        self.assertEqual(current_filter, 'tcp')  # Verifica se o filtro foi definido corretamente

    def test_packet_capture_callback(self):
        """Teste para verificar se o callback de captura de pacotes está sendo chamado."""
        packet_captured = False
        
        def packet_handler(packet):
            nonlocal packet_captured
            packet_captured = True
        
        self.packet_capture.set_callback(packet_handler)
        self.packet_capture.start_capture(timeout=1)  # Captura por 1 segundo
        self.packet_capture.stop_capture()

        self.assertTrue(packet_captured)  # Verifica se o callback foi chamado

if __name__ == '__main__':
    unittest.main()
