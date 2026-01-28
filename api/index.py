from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

app = FastAPI(
      title="Decepticon API",
      version="0.1.0",
      description="Autonomous Multi-Agent Based Red Team Testing Service"
)

@app.get("/")
async def root():
      return {
                "message": "Decepticon API is running",
                "status": "healthy",
                "service": "AI-powered Red Team Testing"
      }

@app.get("/health")
async def health():
      return {"status": "healthy"}

@app.get("/api/status")
async def api_status():
      return {
                "api_version": "0.1.0",
                "framework": "FastAPI",
                "deployment": "Vercel"
      }
