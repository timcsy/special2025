#!/bin/bash

echo "=== 台南家齊高中特色招生查詢系統 Docker 部署工具 ==="
echo

# 檢查 Docker 是否安裝
if ! command -v docker &> /dev/null; then
    echo "[錯誤] 找不到 Docker，請先安裝 Docker。"
    echo "      下載: https://www.docker.com/products/docker-desktop"
    exit 1
fi

echo "[注意] 本部署會使用已準備好的資料庫，不會再次從Excel匯入資料。"

# 檢查 .env 檔案
if [ ! -f .env ]; then
    echo "[警告] 找不到 .env 檔案，將使用預設設定。"
    echo "      建議執行之前先設定 .env 檔案。"
    echo "      包含管理員帳號密碼等重要參數。"
    echo
    read -p "是否繼續? [y/N] " yn
    case $yn in
        [Yy]* ) ;;
        * ) exit;;
    esac
fi

# 建立必要的目錄
echo "[資訊] 建立必要的目錄結構..."
mkdir -p data static media
echo "      完成。"

# 選擇操作
echo
echo "請選擇操作:"
echo "[1] 啟動應用 (docker-compose up)"
echo "[2] 停止應用 (docker-compose down)"
echo "[3] 重建容器 (docker-compose build --no-cache)"
echo "[4] 查看日誌 (docker-compose logs)"
echo "[5] 備份資料庫"
echo "[0] 退出"
echo

read -p "選擇操作 [1-5,0]: " choice

case $choice in
    1)
        echo "[資訊] 啟動應用..."
        docker-compose up -d
        echo "      應用已啟動，請訪問 http://localhost:8000"
        ;;
    2)
        echo "[資訊] 停止應用..."
        docker-compose down
        echo "      應用已停止。"
        ;;
    3)
        echo "[資訊] 重建容器..."
        docker-compose down
        docker-compose build --no-cache
        echo "      容器已重建，請使用選項 1 啟動應用。"
        ;;
    4)
        echo "[資訊] 顯示日誌..."
        docker-compose logs
        echo "      按 Ctrl+C 退出日誌查看。"
        ;;
    5)
        mkdir -p backups
        echo "[資訊] 備份資料庫..."
        cp data/db.sqlite3 "backups/db_$(date +%Y%m%d).sqlite3"
        echo "      資料庫已備份到 backups 目錄。"
        ;;
    0|*)
        exit 0
        ;;
esac
