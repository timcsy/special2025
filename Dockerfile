FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    default-libmysqlclient-dev \
    python3-dev \
    libpq-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libffi-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Python 依賴
COPY requirements.txt .
# 先安裝 numpy 以避免 pandas 安裝問題
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir numpy==1.24.3
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案到容器
COPY . .

# 為啟動腳本添加執行權限
RUN chmod +x /app/entrypoint.sh

# 對外開放 8000 連接埠
EXPOSE 8000

# 設定進入點腳本
ENTRYPOINT ["/app/entrypoint.sh"]
