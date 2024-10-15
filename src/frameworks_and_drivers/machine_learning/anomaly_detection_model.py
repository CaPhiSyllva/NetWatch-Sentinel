import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class AnomalyDetectionModel:
    """
    Classe para detectar anomalias em dados de tráfego de rede.
    """

    def __init__(self):
        """
        Inicializa o modelo de detecção de anomalias.
        """
        self.model = IsolationForest(contamination=0.1)  # Ajuste a contaminação conforme necessário
        self.scaler = StandardScaler()

    def fit(self, data):
        """
        Ajusta o modelo aos dados fornecidos.

        :param data: DataFrame contendo os dados de tráfego de rede.
        """
        # Escala os dados
        scaled_data = self.scaler.fit_transform(data)
        self.model.fit(scaled_data)

    def predict(self, data):
        """
        Prediz se os dados são anômalos.

        :param data: DataFrame contendo os dados de tráfego a serem avaliados.
        :return: Array de -1 (anômalo) ou 1 (normal).
        """
        # Escala os dados
        scaled_data = self.scaler.transform(data)
        return self.model.predict(scaled_data)

    def detect_anomalies(self, data):
        """
        Detecta anomalias nos dados fornecidos.

        :param data: DataFrame contendo os dados de tráfego a serem avaliados.
        :return: DataFrame com a coluna de anomalias adicionada.
        """
        predictions = self.predict(data)
        data['anomaly'] = np.where(predictions == -1, True, False)
        return data

# Exemplo de uso
if __name__ == "__main__":
    # Dados simulados de tráfego de rede
    data = {
        'source_ip': ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5'],
        'destination_ip': ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5'],
        'packet_size': [500, 600, 700, 8000, 600],  # 8000 é uma anomalia
        'duration': [1, 2, 3, 10, 2]
    }

    df = pd.DataFrame(data)

    # Inicializando e ajustando o modelo
    anomaly_model = AnomalyDetectionModel()
    anomaly_model.fit(df[['packet_size', 'duration']])  # Treine apenas com as colunas relevantes

    # Detectando anomalias
    results = anomaly_model.detect_anomalies(df[['packet_size', 'duration']])
    print(results)
