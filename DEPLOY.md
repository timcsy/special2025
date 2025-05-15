# 台南家齊高中特色招生查詢系統 Docker 部署指南

## 部署前準備

### 系統需求

- Docker 和 Docker Compose 已安裝
- 可訪問的伺服器（建議：2GB RAM、1 CPU、20GB 存儲空間）
- 已配置網域名稱（可選）

### 配置環境變數

編輯 `.env` 檔案，根據您的環境設定以下參數：

```properties
# 管理員帳號設定
ADMIN_USERNAME=admin
ADMIN_PASSWORD=安全的密碼
ADMIN_EMAIL=admin@example.com

# 資料庫設定
DATABASE_PATH=/app/data/db.sqlite3

# Django 設定
DEBUG=False
SECRET_KEY=長且複雜的隨機字符串
ALLOWED_HOSTS=localhost,127.0.0.1,您的網域名稱

# 服務埠號
PORT=8000
```

> 注意：部署到生產環境前，請確保更改預設密碼和生成新的 SECRET_KEY。

## 快速部署步驟

### 1. 輕鬆一鍵部署

在專案根目錄執行：

```bash
docker-compose up -d
```

首次部署時，系統會：
- 建立 Docker 容器
- 初始化資料庫
- 建立管理員帳號
- 啟動網站服務

### 2. 使用已有資料庫

如果您已有資料庫檔案，可以將其放在 `data` 目錄下，並確保 `.env` 中的 `DATABASE_PATH` 指向該檔案。

### 3. 檢視日誌

查看應用程式日誌：

```bash
docker-compose logs -f web
```

## 進階配置

### 使用 Nginx 作為反向代理

建議在生產環境中使用 Nginx 作為反向代理，配置 SSL 證書。
以下是基本的 Nginx 配置示例：

```nginx
server {
    listen 80;
    server_name 您的網域名稱;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /path/to/your/project/static/;
    }

    location /media/ {
        alias /path/to/your/project/media/;
    }
}
```

### 資料備份

定期備份資料庫：

```bash
# 方法一：複製資料庫檔案
cp ./data/db.sqlite3 ./backups/db_$(date +%Y%m%d).sqlite3

# 方法二：使用 Django 的 dumpdata 命令
docker-compose exec web python manage.py dumpdata > ./backups/backup_$(date +%Y%m%d).json
```

## 故障排除

### 常見問題

1. **無法連接到服務**
   - 檢查防火牆設定，確保容器端口已開放
   - 確認 `.env` 中的 `ALLOWED_HOSTS` 包含您的網域或 IP

2. **管理員帳號問題**
   - 重設管理員密碼：
     ```bash
     docker-compose exec web python manage.py changepassword admin
     ```

3. **資料庫問題**
   - 如果遇到資料庫相關問題，可以檢查資料庫連接：
     ```bash
     docker-compose exec web python manage.py inspectdb
     ```

## 安全建議

- 定期更新 Docker 鏡像和依賴項
- 使用強密碼和安全的 SECRET_KEY
- 啟用 HTTPS 加密通訊
- 限制管理後台的 IP 訪問
- 定期備份資料庫
