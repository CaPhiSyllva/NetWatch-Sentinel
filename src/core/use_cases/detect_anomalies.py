import numpy as np
from core.entities.network_traffic import NetworkTraffic

class AnomalyDetection:
    """
    Classe responsável pela detecção de anomalias no tráfego de rede.
    """

    def __init__(self, threshold=2.0):
        """
        Inicializa o mecanismo de detecção de anomalias.

        :param threshold: O número de desvios padrão a partir da média para classificar um evento como anômalo.
        """
        self.threshold = threshold
        self.normal_data = []  # Para armazenar dados de tráfego normais

    def update_normal_data(self, traffic_data):
        """
        Atualiza os dados normais com novos dados de tráfego.

        :param traffic_data: Dados do tráfego de rede a serem considerados normais.
        """
        self.normal_data.extend(traffic_data)

    def detect(self, new_traffic):
        """
        Detecta anomalias nos novos dados de tráfego.

        :param new_traffic: Dados do tráfego de rede a serem analisados.
        :return: Lista de anomalias detectadas.
        """
        anomalies = []

        # Calcular média e desvio padrão dos dados normais
        if len(self.normal_data) > 0:
            mean = np.mean(self.normal_data)
            std_dev = np.std(self.normal_data)

            for traffic in new_traffic:
                # Calcular o score Z para o tráfego atual
                z_score = (traffic - mean) / std_dev

                # Se o score Z for maior que o limite, é uma anomalia
                if abs(z_score) > self.threshold:
                    anomalies.append(traffic)

        return anomalies


# Exemplo de uso
if __name__ == "__main__":
    # Inicializando a detecção de anomalias
    anomaly_detector = AnomalyDetection(threshold=2.0)

    # Dados normais simulados (ex: latências em ms)
    normal_traffic_data = [100, 102, 98, 101, 99, 100, 103, 97, 104, 100]
    anomaly_detector.update_normal_data(normal_traffic_data)

    # Novos dados de tráfego para verificar
    new_traffic_data = [101, 105, 110, 95, 200]  # 200 é uma anomalia esperada

    # Detectando anomalias
    detected_anomalies = anomaly_detector.detect(new_traffic_data)

    if detected_anomalies:
        print("Anomalias detectadas:")
        for anomaly in detected_anomalies:
            print(f"Anomalia detectada: {anomaly}")
    else:
        print("Nenhuma anomalia detectada.")
