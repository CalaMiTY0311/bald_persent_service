#!/bin/bash
set -x

echo "===== Docker 확인 및 설치 ====="
echo "Current directory: $(pwd)"

if ! docker --version 2>/dev/null; then
    echo "Installing Docker..."
    sudo apt-get update || exit 1
    sudo apt-get install -y docker.io || exit 1
    sudo systemctl start docker || exit 1
    sudo systemctl enable docker || exit 1
    echo "Docker installed!"
else
    echo "Docker already exists"
    docker --version
fi

if ! docker-compose --version 2>/dev/null; then
    echo "Installing Docker Compose..."
    sudo apt-get install -y docker-compose || exit 1
    echo "Docker Compose installed!"
else
    echo "Docker Compose already exists"
    docker-compose --version
fi

echo "Process completed!"

sudo docker-compose down || true
sudo docker-compose up -d
sudo docker-compose ps