#!/usr/bin/env bash
set -e

echo "========================================================"
echo "   TRAVELMATE AI - Launching System"
echo "   Hybrid Machine Learning & Multi-Objective Travel Planning"
echo "========================================================"

echo "[1/2] Starting FastAPI Backend on http://localhost:8000..."
python3 -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload &
BACKEND_PID=$!

sleep 2

echo "[2/2] Starting React + Vite Frontend on http://localhost:5173..."
cd frontend && npm run dev &
FRONTEND_PID=$!

trap "kill $BACKEND_PID $FRONTEND_PID" EXIT

echo "========================================================"
echo "   TravelMate AI is active!"
echo "   Backend API Docs: http://localhost:8000/docs"
echo "   Frontend Web UI:  http://localhost:5173"
echo "========================================================"

wait
