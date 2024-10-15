#!/bin/bash

# Ativar ambiente virtual
source netwatch_venv/bin/activate

# Verificar se o ambiente virtual foi ativado
if [ $? -ne 0 ]; then
    echo "Erro ao ativar o ambiente virtual. Verifique se o caminho está correto."
    exit 1
fi

# Executar testes
echo "Executando testes..."
pytest tests/ --maxfail=1 --disable-warnings -q

# Verificar o resultado dos testes
if [ $? -eq 0 ]; then
    echo "Todos os testes passaram!"
else
    echo "Alguns testes falharam. Verifique os logs acima."
    exit 1
fi

# Desativar ambiente virtual
deactivate
