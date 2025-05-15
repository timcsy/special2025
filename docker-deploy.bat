@echo off
echo === 台南家齊高中特色招生查詢系統 Docker 部署工具 ===
echo.

REM 檢查 Docker 是否安裝
docker --version > nul 2>&1
if %errorlevel% neq 0 (
    echo [錯誤] 找不到 Docker，請先安裝 Docker。
    echo       下載: https://www.docker.com/products/docker-desktop
    goto :eof
)

echo [注意] 本部署會使用已準備好的資料庫，不會再次從Excel匯入資料。

REM 檢查 .env 檔案
if not exist .env (
    echo [警告] 找不到 .env 檔案，將使用預設設定。
    echo       建議執行之前先設定 .env 檔案。
    echo       包含管理員帳號密碼等重要參數。
    echo.
    echo 是否繼續? [Y/N]
    choice /c YN /m "選擇"
    if errorlevel 2 goto :eof
)

REM 建立必要的目錄
echo [資訊] 建立必要的目錄結構...
if not exist data mkdir data
if not exist static mkdir static
if not exist media mkdir media
echo       完成。

REM 選擇操作
echo.
echo 請選擇操作:
echo [1] 啟動應用 (docker-compose up)
echo [2] 停止應用 (docker-compose down)
echo [3] 重建容器 (docker-compose build --no-cache)
echo [4] 查看日誌 (docker-compose logs)
echo [5] 備份資料庫
echo [0] 退出
echo.

choice /c 123450 /m "選擇操作"

if errorlevel 6 goto :eof
if errorlevel 5 goto backup
if errorlevel 4 goto logs
if errorlevel 3 goto rebuild
if errorlevel 2 goto down
if errorlevel 1 goto up

:up
echo [資訊] 啟動應用...
docker-compose up -d
echo       應用已啟動，請訪問 http://localhost:8000
goto :eof

:down
echo [資訊] 停止應用...
docker-compose down
echo       應用已停止。
goto :eof

:rebuild
echo [資訊] 重建容器...
docker-compose down
docker-compose build --no-cache
echo       容器已重建，請使用選項 1 啟動應用。
goto :eof

:logs
echo [資訊] 顯示日誌...
docker-compose logs
echo       按 Ctrl+C 退出日誌查看。
goto :eof

:backup
if not exist backups mkdir backups
echo [資訊] 備份資料庫...
copy data\db.sqlite3 backups\db_%date:~0,4%%date:~5,2%%date:~8,2%.sqlite3
echo       資料庫已備份到 backups 目錄。
goto :eof
