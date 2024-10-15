import datetime

class NetworkEvent:
    def __init__(self, timestamp, source_ip, dest_ip, event_type, status):
        """Inicializa um evento de rede.

        Args:
            timestamp (str): O timestamp do evento no formato ISO 8601.
            source_ip (str): O IP de origem do evento.
            dest_ip (str): O IP de destino do evento.
            event_type (str): O tipo de evento (ex: "login_attempt", "file_access").
            status (str): O status do evento (ex: "successful", "failed", "success").
        """
        self.timestamp = self._parse_timestamp(timestamp)
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.event_type = event_type
        self.status = status

    def _parse_timestamp(self, timestamp):
        """Converte a string de timestamp em um objeto datetime.

        Args:
            timestamp (str): O timestamp no formato ISO 8601.

        Returns:
            datetime.datetime: O objeto datetime correspondente ao timestamp.
        """
        return datetime.datetime.fromisoformat(timestamp.replace("Z", "+00:00"))

    def __repr__(self):
        """Representação em string do evento de rede."""
        return (f"NetworkEvent(timestamp={self.timestamp}, source_ip={self.source_ip}, "
                f"dest_ip={self.dest_ip}, event_type={self.event_type}, status={self.status})")

    def to_dict(self):
        """Converte o evento de rede em um dicionário.

        Returns:
            dict: Representação do evento em forma de dicionário.
        """
        return {
            "timestamp": self.timestamp.isoformat(),
            "source_ip": self.source_ip,
            "dest_ip": self.dest_ip,
            "event_type": self.event_type,
            "status": self.status
        }

# Exemplo de uso
if __name__ == "__main__":
    event = NetworkEvent("2024-10-15T10:00:00Z", "192.168.1.1", "192.168.1.2", "login_attempt", "failed")
    print(event)
