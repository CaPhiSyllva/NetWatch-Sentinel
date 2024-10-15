from datetime import datetime

class EndpointTraffic:
    def __init__(self, src_ip, dst_ip, total_packets=0, total_bytes=0, first_seen=None, last_seen=None):
        """
        Entidade que representa o tráfego entre dois endpoints.

        :param src_ip: Endereço IP de origem.
        :param dst_ip: Endereço IP de destino.
        :param total_packets: Total de pacotes transmitidos entre os endpoints.
        :param total_bytes: Total de bytes transmitidos entre os endpoints.
        :param first_seen: Data e hora do primeiro pacote detectado.
        :param last_seen: Data e hora do último pacote detectado.
        """
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.total_packets = total_packets
        self.total_bytes = total_bytes
        self.first_seen = first_seen if first_seen else datetime.now()
        self.last_seen = last_seen if last_seen else datetime.now()

    def update_traffic(self, packet_size):
        """
        Atualiza o tráfego entre os endpoints com base em um novo pacote.

        :param packet_size: Tamanho do pacote em bytes.
        """
        self.total_packets += 1
        self.total_bytes += packet_size
        self.last_seen = datetime.now()

    def __repr__(self):
        return (f"<EndpointTraffic src={self.src_ip} dst={self.dst_ip} "
                f"total_packets={self.total_packets} total_bytes={self.total_bytes} "
                f"first_seen={self.first_seen} last_seen={self.last_seen}>")

    def to_dict(self):
        """
        Converte a entidade para um dicionário para fácil armazenamento e serialização.

        :return: Dicionário com os dados do tráfego entre endpoints.
        """
        return {
            "src_ip": self.src_ip,
            "dst_ip": self.dst_ip,
            "total_packets": self.total_packets,
            "total_bytes": self.total_bytes,
            "first_seen": self.first_seen.isoformat(),
            "last_seen": self.last_seen.isoformat(),
        }

    @staticmethod
    def from_packet(packet):
        """
        Cria uma instância de EndpointTraffic a partir de um pacote Scapy.

        :param packet: Pacote capturado pelo Scapy.
        :return: Instância de EndpointTraffic.
        """
        src_ip = packet[0][1].src
        dst_ip = packet[0][1].dst
        packet_size = len(packet)

        return EndpointTraffic(
            src_ip=src_ip,
            dst_ip=dst_ip,
            total_packets=1,
            total_bytes=packet_size
        )
