echo "===== Docker 확인 및 설치 ====="
cd /home/ubuntu
if ! docker --version 2>/dev/null; then
    echo "Installing Docker..."
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker $USER
    echo "Docker installed!"
else
    echo "Docker already exists"
    docker --version
fi
echo "Process completed!"