@echo off

REM Start backend (FastAPI)
start cmd /k "cd /d . && uvicorn backend:app --reload --port 5000"

REM Start frontend (React)
start cmd /k "cd /d obj-frontend && npm start"