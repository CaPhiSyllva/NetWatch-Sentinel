#!/bin/bash

# Nome da imagem Docker
IMAGE_NAME="netwatch_xdr"
# Tag da imagem (versão)
IMAGE_TAG="latest"

# Construir a imagem Docker
echo "Construindo a imagem Docker: ${IMAGE_NAME}:${IMAGE_TAG}..."

docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .

# Verificar se a construção foi bem-sucedida
if [ $? -eq 0 ]; then
    echo "Imagem Docker ${IMAGE_NAME}:${IMAGE_TAG} criada com sucesso!"
else
    echo "Falha ao criar a imagem Docker."
    exit 1
fi

# Listar as imagens Docker disponíveis
echo "Imagens Docker disponíveis:"
docker images

# Concluir
echo "Processo de construção concluído."
