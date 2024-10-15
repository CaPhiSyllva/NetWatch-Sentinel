from datetime import datetime  

class NetworkTraffic:
    def __init__(self, src_ip, dst_ip, protocol, src_port=None, dst_port=None,payload=None, timestamp=None):
        """Entidade que representa o tráfego de rede capturado.
        
        :param src_ip: Endereço IP de origem
        :param dst_ip: Endereço IP de destino
        :param protocol: Protocolo de transporte(TCP, UDP, ICMP, etc.)
        :param src_port: Porta de origem(opcional, aplicável para TCP/UDP)
        :param dst_port: Porta de destino(opcional, aplicável para TCP/UDP)
        :param payload: Dados de Pacote(opcional)
        :param timestamp: Data e hora da captura do pacote.
        """

        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.protocol = protocol
        self.src_port = src_port
        self.dst_port = dst_port
        self.payload = payload
        self.timestamp = timestamp = timestamp if timestamp else datetime.now()
        
        def __repr__(self):
            return f"<Network Traffic src={self.src_ip} dst ={self.dst_ip} protocol={self.protocol}
            timestamp ={self.timestamp}>"
            
            def to_dict(self):
                """
                Converte a entidade para um dicionário para facilitar o armazenamento ou serialização
                
                :return: Dicionário com os dados do tráfego de rede.
                """
                return{
                    "src_ip":self.src_ip,
                    "dst_ip":self.dst_ip,
                    "protocol":self.protocol,
                    "src_port":self.src_port,
                    "dst_port":self.dst_port,
                    "payload": self.payload,
                    "timestamp": self.timestamp.isoformat()
                    
                }
                
                @staticmethod
                def from_packet(packet):
                    """
                    Cria uma instância de NetworkTraffic a partir de um pacote Scapy,
                    
                    :param packet: Pacote capturado pelo Scapy.
                    :return: Instância de NetworkTraffic.
                    """
                    src_ip = packet[0][1].src
                    dst_ip = packet[0][1].dst
                    protocol = packet[0].proto
                    
                    #Verifica se o protocolo é TCP, UDP, ou ICMP e extrai as portas se aplicável
                    
                    src_port = dst_port = None
                    if protocol ==6: #TCP
                      src_port= packet[0][2].sport
                      dst_port = packet[0][2].dport
                      protocol = "TCP"
                    elif protocol ==17: #UDP
                         src_port= packet[0][2].sport
                         dst_port = packet[0][2].dport 
                         protocol = "UDP" 
                    elif protocol ==1:#ICMP
                         src_port= packet[0][2].sport
                         dst_port = packet[0][2].dport 
                         protocol = "ICMP"
                    
                    payload = bytes(packet[0][2]).hex() if hasattr(packet[0], 'payload') else None
                    
                    return NetworkTraffic(
                        src_ip=src_ip,
                        dst_ip= dst_ip,
                        protocol=protocol,
                        src_port= src_port,
                        dst_port= dst_port,
                        payload= payload
                    ) 