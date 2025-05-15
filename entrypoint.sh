#!/bin/bash

# 確保 data 目錄存在
mkdir -p /app/data

# 判斷是否需要使用外部資料庫檔案
if [ ! -f "$DATABASE_PATH" ] || [ ! -s "$DATABASE_PATH" ]; then
    echo "Setting up a new database or using the specified empty database..."
    # 執行資料庫初始化
    python manage.py migrate
    python manage.py collectstatic --no-input

    # 匯入成績資料
    if [ -f "2025score.xlsx" ]; then
        echo "Importing data from Excel..."
        python manage.py import_data
    else
        echo "Warning: 2025score.xlsx not found!"
    fi

    # 建立管理員帳號 (使用環境變數)
    python manage.py createsuperuser --noinput
else
    echo "Using existing database at $DATABASE_PATH"
    python manage.py migrate
    python manage.py collectstatic --no-input
fi

# 啟動 Gunicorn 伺服器
exec gunicorn special.wsgi:application --bind 0.0.0.0:8000
