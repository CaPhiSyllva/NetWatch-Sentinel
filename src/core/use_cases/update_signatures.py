import requests
from core.entities.attack_signature import AttackSignature

class SignatureUpdater:
    """
    Classe responsável pela atualização das assinaturas de ataques.
    """

    def __init__(self, signature_repository):
        """
        Inicializa o SignatureUpdater com um repositório de assinaturas.

        :param signature_repository: O repositório onde as assinaturas serão armazenadas.
        """
        self.signature_repository = signature_repository

    def fetch_signatures(self, source_url):
        """
        Busca assinaturas de uma fonte externa.

        :param source_url: URL da fonte externa de assinaturas.
        :return: Lista de novas assinaturas.
        """
        try:
            response = requests.get(source_url)
            response.raise_for_status()
            signatures_data = response.json()
            new_signatures = [
                AttackSignature(signature=item["signature"], description=item["description"])
                for item in signatures_data
            ]
            return new_signatures
        except requests.RequestException as e:
            print(f"Erro ao buscar assinaturas: {e}")
            return []

    def update_signatures(self, source_url):
        """
        Atualiza as assinaturas de ataques a partir de uma fonte externa.

        :param source_url: URL da fonte externa de assinaturas.
        """
        new_signatures = self.fetch_signatures(source_url)
        if new_signatures:
            for signature in new_signatures:
                self.signature_repository.add_signature(signature)
            print(f"Atualizadas {len(new_signatures)} assinaturas.")
        else:
            print("Nenhuma nova assinatura encontrada.")

# Exemplo de uso
if __name__ == "__main__":
    class MockSignatureRepository:
        """Um repositório de assinaturas simulado para fins de demonstração."""
        
        def __init__(self):
            self.signatures = []

        def add_signature(self, signature):
            self.signatures.append(signature)
            print(f"Assinatura adicionada: {signature.signature} - {signature.description}")

    # Inicializando o repositório de assinaturas simulado
    mock_repository = MockSignatureRepository()

    # Inicializando o atualizador de assinaturas
    signature_updater = SignatureUpdater(signature_repository=mock_repository)

    # URL da fonte externa de assinaturas (exemplo)
    source_url = "https://example.com/signatures"

    # Atualizando as assinaturas
    signature_updater.update_signatures(source_url)
