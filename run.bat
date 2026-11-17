@echo off
echo ========================================================
echo    TRAVELMATE AI - Launching System
echo    Hybrid Machine Learning and Multi-Objective Travel Planning
echo ========================================================

echo.
echo [1/2] Starting FastAPI Backend on http://localhost:8000...
start "TravelMate AI - Backend" cmd /k "python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload"

timeout /t 2 /nobreak >nul

echo [2/2] Starting React + Vite Frontend on http://localhost:5173...
start "TravelMate AI - Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================================
echo    TravelMate AI is up and running!
echo    Backend API:     http://localhost:8000/docs
echo    Web Application: http://localhost:5173
echo ========================================================
echo.
