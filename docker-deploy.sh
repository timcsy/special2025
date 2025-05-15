#!/bin/bash

echo "=== Tainan Jia-Chi High School Special Enrollment Query System ==="
echo

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "[ERROR] Docker not found. Please install Docker first."
    echo "        Download: https://www.docker.com/products/docker-desktop"
    exit 1
fi

echo "[NOTICE] This deployment will use the prepared database and will not import Excel data again."

# Check .env file
if [ ! -f .env ]; then
    echo "[WARNING] .env file not found, will use default settings."
    echo "          It is recommended to set up the .env file before execution."
    echo "          It contains important parameters like admin credentials."
    echo
    read -p "Continue? [y/N] " yn
    case $yn in
        [Yy]* ) ;;
        * ) exit;;
    esac
fi

# Create necessary directories
echo "[INFO] Creating necessary directory structure..."
mkdir -p data static media
echo "       Done."

# Choose operation
echo
echo "Please select an operation:"
echo "[1] Start application (docker-compose up)"
echo "[2] Stop application (docker-compose down)"
echo "[3] Rebuild container (docker-compose build --no-cache)"
echo "[4] View logs (docker-compose logs)"
echo "[5] Backup database"
echo "[0] Exit"
echo

read -p "Select operation [1-5,0]: " choice

case $choice in
    1)
        echo "[INFO] Starting application..."
        docker-compose up -d
        echo "       Application started, please visit http://localhost:8000"
        ;;
    2)
        echo "[INFO] Stopping application..."
        docker-compose down
        echo "       Application stopped."
        ;;
    3)
        echo "[INFO] Rebuilding container..."
        docker-compose down
        docker-compose build --no-cache
        echo "       Container rebuilt, please use option 1 to start the application."
        ;;
    4)
        echo "[INFO] Displaying logs..."
        docker-compose logs
        echo "       Press Ctrl+C to exit log view."
        ;;
    5)
        mkdir -p backups
        echo "[INFO] Backing up database..."
        cp data/db.sqlite3 "backups/db_$(date +%Y%m%d).sqlite3"
        echo "       Database backed up to backups directory."
        ;;
    0|*)
        exit 0
        ;;
esac
