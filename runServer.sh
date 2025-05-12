#!/usr/bin/env bash
set -e  # 오류 발생 시 스크립트 중단

echo "===== 1. 환경 확인 ====="
echo "현재 사용자: $(whoami)"
echo "현재 디렉토리: $(pwd)"

echo "===== 2. 디렉토리 확인 및 이동 ====="
if [ "$(pwd)" != "/home/ubuntu" ]; then
    echo "Not in /home/ubuntu, moving there..."
    cd /home/ubuntu
    echo "Moved to: $(pwd)"
else
    echo "Already in /home/ubuntu"
fi

echo "===== 3. Docker 설치 확인 ====="
if ! command -v docker &> /dev/null; then
    echo "Docker not found. Installing Docker..."
    
    # 시스템 업데이트
    sudo apt-get update
    
    # 필요한 패키지 설치
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    
    # Docker 공식 GPG 키 추가 (Ubuntu 24.04 호환)
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    
    # Docker 레포지토리 추가
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    # 패키지 목록 업데이트
    sudo apt-get update
    
    # Docker 설치
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
    
    # Docker 서비스 시작
    sudo systemctl start docker
    sudo systemctl enable docker
    
    # 현재 사용자를 docker 그룹에 추가
    sudo usermod -aG docker $USER
    
    echo "Docker installed successfully!"
else
    echo "Docker is already installed"
    docker --version
fi

echo "===== 4. Docker Compose 확인 ====="
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "Docker Compose not found. Installing..."
    # docker-compose-plugin이 이미 위에서 설치되므로 'docker compose' 사용 가능
    sudo apt-get install -y docker-compose
    echo "Docker Compose installed"
else
    echo "Docker Compose is available"
    if command -v docker-compose &> /dev/null; then
        docker-compose --version
    else
        docker compose version
    fi
fi

echo "===== 5. 프로젝트 파일 확인 ====="
ls -la

echo "===== 6. Docker 애플리케이션 배포 ====="
if [ -f "docker-compose.yml" ]; then
    echo "docker-compose.yml found. Starting deployment..."
    
    # 기존 컨테이너 중지
    echo "Stopping existing containers..."
    if command -v docker-compose &> /dev/null; then
        docker-compose down || true
    else
        sudo docker compose down || true
    fi
    
    # 새 이미지 빌드
    echo "Building new image..."
    if command -v docker-compose &> /dev/null; then
        docker-compose build
    else
        sudo docker compose build
    fi
    
    # 컨테이너 시작
    echo "Starting containers..."
    if command -v docker-compose &> /dev/null; then
        docker-compose up -d
    else
        sudo docker compose up -d
    fi
    
    # 상태 확인
    echo "Checking container status..."
    if command -v docker-compose &> /dev/null; then
        docker-compose ps
    else
        sudo docker compose ps
    fi
    
    echo "Deployment completed successfully!"
else
    echo "docker-compose.yml not found! Please check the file exists."
    exit 1
fi

echo "===== 7. 최종 상태 확인 ====="
sudo docker ps
echo "API deployment completed!"