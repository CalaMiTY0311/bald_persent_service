#!/bin/bash
set -x
echo "===== Docker 확인 및 설치 ====="
cd /home/ubuntu || exit 1
echo "Current directory: $(pwd)"
if ! docker --version 2>/dev/null; then
    echo "Installing Docker..."
    sudo apt-get update || exit 1
    sudo apt-get install -y docker.io || exit 1
    sudo systemctl start docker || exit 1
    sudo systemctl enable docker || exit 1
    sudo usermod -aG docker $USER || exit 1
    echo "Docker installed!"
else
    echo "Docker already exists"
    docker --version
fi
echo "Process completed!"