#!/bin/sh

# 確保 data 目錄存在
mkdir -p /app/data

# 確保score/static目錄存在
mkdir -p /app/score/static/js
touch /app/score/static/__init__.py
touch /app/score/static/js/__init__.py

# 判斷是否需要使用外部資料庫檔案
if [ ! -f "$DATABASE_PATH" ] || [ ! -s "$DATABASE_PATH" ]; then
    echo "設定新資料庫或使用指定的空資料庫..."
    # 執行資料庫初始化
    python manage.py migrate
    
    # 強制複製靜態文件
    echo "收集靜態檔案..."
    python manage.py collectstatic --no-input --clear

    # 建立管理員帳號 (使用環境變數)
    echo "創建管理員帳號: $DJANGO_SUPERUSER_USERNAME"
    python manage.py createsuperuser --noinput || echo "管理員帳號可能已存在，繼續執行..."
else
    echo "使用現有資料庫: $DATABASE_PATH"
    python manage.py migrate
    
    # 強制複製靜態文件
    echo "收集靜態檔案..."
    python manage.py collectstatic --no-input --clear
fi

# 檢查靜態檔案是否存在
if [ -f "/app/static/js/form-handler.js" ]; then
    echo "靜態檔案已成功收集"
else
    echo "警告：靜態檔案收集可能失敗"
fi

# 啟動 Gunicorn 伺服器
echo "Starting server at 0.0.0.0:8000..."
exec gunicorn special.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --threads 4 \
    --worker-class=gthread \
    --worker-tmp-dir /dev/shm \
    --timeout 120 \
    --log-level info
