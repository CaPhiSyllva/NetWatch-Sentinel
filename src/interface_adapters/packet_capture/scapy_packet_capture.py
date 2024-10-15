from scapy.all import sniff, IP, TCP, UDP, ICMP, ARP
from src.config.settings import settings
import logging

#Configurações de logging
logging.basicConfig(level= settings.get_logging_config()["level"])
logger = logging.getLogger(__name__)

class PacketCapture:
    def __init__(self, interface=settings.network_interface,packet_filter=settings.packet_capture_filter):
        self.interface = interface
        self.packet_filter = packet_filter
        logger.info(f"Inicializando captura de pacotes na rede: {self.interface}")
        logger.info(f"Filtros de pacote aplicado: {self.packet_filter}")
        
    def packet_handler(self, packet):
        """Função chamada sempre que um pacote é capturado"""
        if packet.haslayer(IP):
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            
            if packet.haslayer(TCP):
                logger.info(f"TCP Packet: {ip_src} -> {ip_dst}(Port: {packet[TCP].sport} -> {packet[TCP].dport})")
            elif packet.haslayer(UDP):
                logger.info(f"UDP Packet: {ip_src} -> {ip_dst}(Port: {packet[UDP].sport} -> {packet[UDP].dport})")
            elif packet.haslayer(ICMP):
                logger.info(f"ICMP Packet: {ip_src}->{ip_dst}")
            elif packet.haslayer(ARP):
                arp_psrc = packet[ARP].psrc
                arp_pdst = packet[ARP].pdst
                logger.info(f"ARP Packet: {arp_psrc} -> {arp_pdst}")
    def start_capture(self):
        """Metódo para iniciar a captura de pacotes"""
        try:
            logger.info(f"Iniciando captura de pacotes na interface {self.interface} com o filtro '{self.packet_filter}'")
            sniff(iface=self.interface, filter=self.packet_filter, prn=self.packet_handler, store =0)
        except Exception as e:
            logger.error(f"Erro ao capturar pacotes: {e}")

if __name__ == "__main__":
    packet_capture = PacketCapture()
    packet_capture.start_capture()