@echo off
setlocal

echo ==========================================
echo Starting TestGenX Application
echo ==========================================

REM ---- Start Backend in background ----
start /B cmd /c "cd backend && call .venv\Scripts\activate && uvicorn main:app --host 0.0.0.0 --port 9091"

timeout /t 5 > nul

REM ---- Start Frontend in same window ----
cd frontend


start "" "http://localhost:9090"
echo.
echo ==========================================
echo Backend  : http://localhost:9091
echo Swagger  : http://localhost:9091/docs
echo Frontend : http://localhost:9090
echo ==========================================
echo.
npm run dev -- --port 9090