#!/bin/bash

# Atualizar pacotes e instalar Python e pip, se não estiverem instalados
echo "Atualizando pacotes do sistema..."
sudo apt-get update

echo "Instalando Python e pip..."
sudo apt-get install -y python3 python3-pip python3-venv

# Criar e ativar um ambiente virtual
echo "Criando ambiente virtual..."
python3 -m venv netwatch_venv

echo "Ativando ambiente virtual..."
source netwatch_venv/bin/activate

# Instalar dependências
echo "Instalando dependências..."
pip install -r requirements.txt

# Configurar variáveis de ambiente
echo "Configurando variáveis de ambiente..."
export FLASK_HOST='0.0.0.0'
export FLASK_PORT='5000'
export NETWORK_INTERFACE='any'
export PACKET_CAPTURE_FILTER='tcp or udp or icmp or arp'
export ANOMALY_MODEL_PATH='models/anomaly_detection_model.pkl'
export THREAT_INTELLIGENCE_API_KEY='your-api-key'
export ELASTICSEARCH_URL='http://localhost:9200'
export LOG_LEVEL='INFO'
export ENVIRONMENT='development'
export AUTO_UPDATE_SIGNATURES='true'

echo "Configuração do ambiente concluída!"

# Lembrete para o usuário
echo "Para ativar o ambiente virtual, execute 'source netwatch_venv/bin/activate'."
echo "Para iniciar o Flask, execute 'python flask_dashboard.py'."
