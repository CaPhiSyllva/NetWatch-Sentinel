import subprocess
import json
import logging
from settings import settings

# Configurando o logger
logging.basicConfig(level=settings.log_level)
logger = logging.getLogger(__name__)

class OsqueryAdapter:
    def __init__(self):
        self.osquery_bin = 'osqueryi'  # Caminho do binário do Osquery

    def execute_query(self, query: str) -> dict:
        """Executa uma consulta no Osquery e retorna os resultados em formato JSON."""
        try:
            # Executa a consulta no Osquery
            process = subprocess.Popen(
                [self.osquery_bin, '--json', '-A', query],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = process.communicate()

            # Verifica se houve erro na execução da consulta
            if process.returncode != 0:
                logger.error("Erro ao executar consulta Osquery: %s", stderr.decode())
                return {"error": stderr.decode()}

            # Carrega os resultados em formato JSON
            results = json.loads(stdout.decode())
            logger.info("Consulta Osquery executada com sucesso: %s", results)
            return results
        except Exception as e:
            logger.exception("Ocorreu uma exceção ao executar a consulta Osquery: %s", str(e))
            return {"error": str(e)}

    def get_running_processes(self) -> dict:
        """Obtém uma lista de processos em execução no sistema."""
        query = "SELECT * FROM processes;"
        return self.execute_query(query)

    def get_system_info(self) -> dict:
        """Obtém informações do sistema."""
        query = "SELECT * FROM system_info;"
        return self.execute_query(query)

    def get_installed_packages(self) -> dict:
        """Obtém a lista de pacotes instalados."""
        query = "SELECT * FROM deb_packages;"  # Para sistemas baseados em Debian
        return self.execute_query(query)

# Exemplo de uso
if __name__ == "__main__":
    osquery_adapter = OsqueryAdapter()
    
    # Exemplo de execução de uma consulta
    running_processes = osquery_adapter.get_running_processes()
    print("Processos em execução:", running_processes)

    # Obtendo informações do sistema
    system_info = osquery_adapter.get_system_info()
    print("Informações do sistema:", system_info)

    # Obtendo pacotes instalados
    installed_packages = osquery_adapter.get_installed_packages()
    print("Pacotes instalados:", installed_packages)
