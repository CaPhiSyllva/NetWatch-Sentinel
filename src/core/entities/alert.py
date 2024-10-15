from datetime import datetime

class Alert:
    def __init__(self, alert_id, alert_type, severity, description, source_ip, destination_ip, timestamp=None):
        """
        Entidade que representa um alerta gerado pelo sistema de detecção.

        :param alert_id: ID único do alerta.
        :param alert_type: Tipo do alerta (ex.: 'Anomalia', 'Assinatura', 'Tentativa de Intrusão').
        :param severity: Nível de severidade do alerta (ex.: 'Baixo', 'Médio', 'Alto', 'Crítico').
        :param description: Descrição do alerta e contexto.
        :param source_ip: Endereço IP de origem envolvido no alerta.
        :param destination_ip: Endereço IP de destino envolvido no alerta.
        :param timestamp: Data e hora do alerta gerado. Se não fornecido, utiliza o momento atual.
        """
        self.alert_id = alert_id
        self.alert_type = alert_type
        self.severity = severity
        self.description = description
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.timestamp = timestamp if timestamp else datetime.now()

    def __repr__(self):
        return (f"<Alert id={self.alert_id} type={self.alert_type} severity={self.severity} "
                f"description={self.description} source_ip={self.source_ip} destination_ip={self.destination_ip} "
                f"timestamp={self.timestamp}>")

    def to_dict(self):
        """
        Converte a entidade Alert em um dicionário para facilitar o armazenamento e serialização.

        :return: Dicionário com os dados do alerta.
        """
        return {
            "alert_id": self.alert_id,
            "alert_type": self.alert_type,
            "severity": self.severity,
            "description": self.description,
            "source_ip": self.source_ip,
            "destination_ip": self.destination_ip,
            "timestamp": self.timestamp.isoformat(),
        }

    @staticmethod
    def from_event(event_data):
        """
        Cria um alerta a partir de dados de um evento.

        :param event_data: Dicionário contendo os dados do evento de rede ou de ataque.
        :return: Instância de Alert gerada a partir dos dados do evento.
        """
        return Alert(
            alert_id=event_data.get("alert_id"),
            alert_type=event_data.get("alert_type"),
            severity=event_data.get("severity"),
            description=event_data.get("description"),
            source_ip=event_data.get("source_ip"),
            destination_ip=event_data.get("destination_ip"),
            timestamp=event_data.get("timestamp", None)
        )
