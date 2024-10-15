from core.entities.alert import Alert
from core.entities.network_traffic import NetworkTraffic

class EventCorrelation:
    """
    Classe responsável pela correlação de eventos de segurança.
    """

    def __init__(self):
        self.events = []  # Lista para armazenar eventos a serem correlacionados

    def add_event(self, event):
        """
        Adiciona um evento à lista de eventos.

        :param event: O evento a ser adicionado, que pode ser um objeto NetworkTraffic ou Alert.
        """
        self.events.append(event)

    def correlate(self):
        """
        Realiza a correlação de eventos.

        :return: Lista de alertas gerados a partir da correlação de eventos.
        """
        correlated_alerts = []
        # Exemplo simples de correlação
        for i in range(len(self.events)):
            for j in range(i + 1, len(self.events)):
                event_a = self.events[i]
                event_b = self.events[j]

                # Verifica se os eventos têm características que possam estar relacionadas
                if isinstance(event_a, NetworkTraffic) and isinstance(event_b, Alert):
                    if self.is_related(event_a, event_b):
                        correlated_alerts.append(self.create_alert(event_a, event_b))

        return correlated_alerts

    def is_related(self, traffic_event, alert_event):
        """
        Verifica se o evento de tráfego e o alerta estão relacionados.

        :param traffic_event: Evento de tráfego.
        :param alert_event: Alerta gerado.
        :return: Verdadeiro se os eventos estão relacionados, falso caso contrário.
        """
        # Implementar a lógica de correlação aqui (exemplo fictício)
        return (traffic_event.source_ip == alert_event.source_ip and
                traffic_event.destination_ip == alert_event.destination_ip)

    def create_alert(self, traffic_event, alert_event):
        """
        Cria um alerta baseado na correlação entre um evento de tráfego e um alerta.

        :param traffic_event: Evento de tráfego.
        :param alert_event: Alerta gerado.
        :return: Um novo alerta correlacionado.
        """
        correlated_alert = Alert(
            source_ip=traffic_event.source_ip,
            destination_ip=traffic_event.destination_ip,
            severity=alert_event.severity,
            message=f"Correlated event: {alert_event.message} with traffic from {traffic_event.source_ip} to {traffic_event.destination_ip}"
        )
        return correlated_alert


# Exemplo de uso
if __name__ == "__main__":
    # Inicializando a correlação de eventos
    event_correlation = EventCorrelation()

    # Criando eventos de exemplo
    traffic_event = NetworkTraffic(source_ip="192.168.1.1", destination_ip="10.0.0.1", timestamp="2024-10-15T10:00:00Z")
    alert_event = Alert(source_ip="192.168.1.1", destination_ip="10.0.0.1", severity="high", message="Possible intrusion detected")

    # Adicionando eventos
    event_correlation.add_event(traffic_event)
    event_correlation.add_event(alert_event)

    # Realizando a correlação
    correlated_alerts = event_correlation.correlate()

    # Exibindo alertas correlacionados
    if correlated_alerts:
        print("Alertas correlacionados:")
        for alert in correlated_alerts:
            print(f"Alerta: {alert.message}, Severidade: {alert.severity}")
    else:
        print("Nenhum alerta correlacionado detectado.")
