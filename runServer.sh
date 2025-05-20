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

echo "기존 컨테이너 중지 중..."
sudo docker-compose down || true

echo "도커 이미지 다시 빌드 중..."
sudo docker-compose build || echo "빌드 중 경고가 있지만 계속 진행합니다."

echo "업데이트된 컨테이너 시작 중..."
sudo docker-compose up -d
# sudo docker rm -f ubuntu_talmoapi
