"""
Blood Bank Management System - Local Runner
Starts the Uvicorn ASGI server hosting the FastAPI application.
"""
import os
import uvicorn

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    print(f"============================================================")
    print(f"  BloodBank Live™ Management System")
    print(f"  Local Access:   http://localhost:{port}")
    print(f"  Network Access: http://0.0.0.0:{port}")
    print(f"  API Docs:       http://localhost:{port}/docs")
    print(f"============================================================")
    uvicorn.run("app.main:app", host=host, port=port, reload=True)
