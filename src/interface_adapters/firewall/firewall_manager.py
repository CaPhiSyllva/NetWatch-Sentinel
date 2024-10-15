import logging
import subprocess
import platform

# Importando as configurações
from settings import settings

# Configurando o logger
logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)

class FirewallManager:
    def __init__(self):
        self.os_type = platform.system()
        if self.os_type == 'Linux':
            self.firewall_command = 'iptables'
        elif self.os_type == 'Windows':
            self.firewall_command = 'netsh advfirewall firewall'
        else:
            logger.error("Sistema operacional não suportado.")
            raise NotImplementedError("O gerenciamento de firewall não é suportado neste sistema operacional.")

    def add_rule(self, rule: str) -> bool:
        """Adiciona uma nova regra ao firewall."""
        try:
            if self.os_type == 'Linux':
                subprocess.run([self.firewall_command, '-A', 'INPUT', '-p', rule], check=True)
                logger.info("Regra adicionada com sucesso (Linux): %s", rule)
            elif self.os_type == 'Windows':
                subprocess.run([self.firewall_command, 'add', 'rule', 'name={}'.format(rule), 'dir=in', 'action=allow'], check=True)
                logger.info("Regra adicionada com sucesso (Windows): %s", rule)
            return True
        except subprocess.CalledProcessError as e:
            logger.error("Erro ao adicionar regra: %s", e)
            return False

    def remove_rule(self, rule: str) -> bool:
        """Remove uma regra do firewall."""
        try:
            if self.os_type == 'Linux':
                subprocess.run([self.firewall_command, '-D', 'INPUT', '-p', rule], check=True)
                logger.info("Regra removida com sucesso (Linux): %s", rule)
            elif self.os_type == 'Windows':
                subprocess.run([self.firewall_command, 'delete', 'rule', 'name={}'.format(rule)], check=True)
                logger.info("Regra removida com sucesso (Windows): %s", rule)
            return True
        except subprocess.CalledProcessError as e:
            logger.error("Erro ao remover regra: %s", e)
            return False

    def list_rules(self) -> None:
        """Lista todas as regras do firewall."""
        try:
            if self.os_type == 'Linux':
                result = subprocess.run([self.firewall_command, '-L'], check=True, capture_output=True, text=True)
                logger.info("Regras do firewall (Linux):\n%s", result.stdout)
            elif self.os_type == 'Windows':
                result = subprocess.run([self.firewall_command, 'show', 'rule'], check=True, capture_output=True, text=True)
                logger.info("Regras do firewall (Windows):\n%s", result.stdout)
        except subprocess.CalledProcessError as e:
            logger.error("Erro ao listar regras: %s", e)

# Exemplo de uso
if __name__ == "__main__":
    firewall_manager = FirewallManager()

    # Adicionar uma regra
    firewall_manager.add_rule("tcp --dport 22")  # Permitir acesso SSH no Linux ou por nome no Windows

    # Remover uma regra
    firewall_manager.remove_rule("tcp --dport 22")  # Remover a mesma regra

    # Listar regras
    firewall_manager.list_rules()
