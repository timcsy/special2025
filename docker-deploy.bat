@echo off
chcp 65001 > nul
echo === Tainan Jia-Chi High School Special Enrollment Query System ===
echo.

REM Check if Docker is installed
docker --version > nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker not found. Please install Docker first.
    echo         Download: https://www.docker.com/products/docker-desktop
    goto :eof
)

echo [NOTICE] This deployment will use the prepared database and will not import Excel data again.

REM Check .env file
if not exist .env (
    echo [WARNING] .env file not found, will use default settings.
    echo           It is recommended to set up the .env file before execution.
    echo           It contains important parameters like admin credentials.
    echo.
    echo Continue? [Y/N]
    choice /c YN /m "Select"
    if errorlevel 2 goto :eof
)

REM Create necessary directories
echo [INFO] Creating necessary directory structure...
if not exist data mkdir data
if not exist static mkdir static
if not exist media mkdir media
echo       Done.

REM Choose operation
echo.
echo Please select an operation:
echo [1] Start application (docker-compose up)
echo [2] Stop application (docker-compose down)
echo [3] Rebuild container (docker-compose build --no-cache)
echo [4] View logs (docker-compose logs)
echo [5] Backup database
echo [0] Exit
echo.

choice /c 123450 /m "Select operation"

if errorlevel 6 goto :eof
if errorlevel 5 goto backup
if errorlevel 4 goto logs
if errorlevel 3 goto rebuild
if errorlevel 2 goto down
if errorlevel 1 goto up

:up
echo [INFO] Starting application...
docker-compose up -d
echo       Application started, please visit http://localhost:8000
goto :eof

:down
echo [INFO] Stopping application...
docker-compose down
echo       Application stopped.
goto :eof

:rebuild
echo [INFO] Rebuilding container...
docker-compose down
docker-compose build --no-cache
echo       Container rebuilt, please use option 1 to start the application.
goto :eof

:logs
echo [INFO] Displaying logs...
docker-compose logs
echo       Press Ctrl+C to exit log view.
goto :eof

:backup
if not exist backups mkdir backups
echo [INFO] Backing up database...
copy data\db.sqlite3 backups\db_%date:~0,4%%date:~5,2%%date:~8,2%.sqlite3
echo       Database backed up to backups directory.
goto :eof
