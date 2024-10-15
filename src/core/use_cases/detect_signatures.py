from core.entities.attack_signature import AttackSignature

class SignatureDetection:
    """
    Classe responsável pela detecção de ataques baseados em assinaturas de padrões maliciosos.
    """

    def __init__(self, signatures):
        """
        Inicializa o mecanismo de detecção de assinaturas.

        :param signatures: Lista de assinaturas de ataques conhecidas.
        """
        self.signatures = signatures

    def detect(self, network_data):
        """
        Detecta assinaturas conhecidas no tráfego de rede.

        :param network_data: Dados do tráfego de rede a serem analisados.
        :return: Lista de assinaturas detectadas (caso alguma corresponda ao tráfego).
        """
        detected_signatures = []
        for signature in self.signatures:
            if signature.match(network_data):
                detected_signatures.append(signature.get_details())
        return detected_signatures


# Exemplo de uso
if __name__ == "__main__":
    # Definindo algumas assinaturas de exemplo
    ddos_signature = AttackSignature(
        signature_id=1,
        name="DDoS Attack",
        description="Detecção de ataque de negação de serviço distribuído (DDoS).",
        pattern="大量的请求",  # Padrão para tráfego DDoS (simulado)
        severity="Alto",
        mitigation="Bloquear IP de origem, ajustar firewall."
    )

    port_scan_signature = AttackSignature(
        signature_id=2,
        name="Port Scan",
        description="Detecção de varredura de portas em hosts de rede.",
        pattern="SYN_SCAN",  # Exemplo de padrão para escaneamento de portas
        severity="Médio",
        mitigation="Monitorar atividades e ajustar regras de firewall."
    )

    # Instanciando o mecanismo de detecção com as assinaturas conhecidas
    signatures = [ddos_signature, port_scan_signature]
    detector = SignatureDetection(signatures)

    # Dados simulados de tráfego de rede
    simulated_traffic = "大量的请求"

    # Detectando assinaturas no tráfego
    detected_attacks = detector.detect(simulated_traffic)

    if detected_attacks:
        print("Assinaturas detectadas:")
        for attack in detected_attacks:
            print(attack)
    else:
        print("Nenhuma assinatura de ataque detectada.")
