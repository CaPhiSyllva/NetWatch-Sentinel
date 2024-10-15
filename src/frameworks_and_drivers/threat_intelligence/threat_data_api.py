import requests
from settings import Settings

class ThreatDataAPI:
    def __init__(self):
        self.virustotal_api_key = Settings.VIRUSTOTAL_API_KEY
        self.otx_api_key = Settings.OTX_API_KEY
        self.otx_base_url = "https://otx.alienvault.com/api/v1/"

    def get_virustotal_report(self, resource):
        """Obtém um relatório do VirusTotal para um arquivo, URL, IP ou domínio."""
        url = f"https://www.virustotal.com/api/v3/analyses/{resource}"
        headers = {
            "x-apikey": self.virustotal_api_key
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching from VirusTotal: {response.status_code} - {response.text}")
            return None

    def get_otx_indicator(self, indicator):
        """Obtém informações sobre um indicador de ameaça do AlienVault OTX."""
        url = f"{self.otx_base_url}indicators/lookup"
        headers = {
            "X-OTX-API-KEY": self.otx_api_key
        }
        params = {
            "indicator": indicator
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching from OTX: {response.status_code} - {response.text}")
            return None

# Exemplo de uso
if __name__ == "__main__":
    threat_api = ThreatDataAPI()
    
    # Obtendo um relatório do VirusTotal
    vt_resource = "YOUR_RESOURCE"  # Substitua por um hash, URL ou domínio real
    vt_report = threat_api.get_virustotal_report(vt_resource)
    print("VirusTotal Report:", vt_report)

    # Obtendo informações do AlienVault OTX
    otx_indicator = "YOUR_INDICATOR"  # Substitua por um IP ou domínio real
    otx_report = threat_api.get_otx_indicator(otx_indicator)
    print("AlienVault OTX Report:", otx_report)
