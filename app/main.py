from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router

app = FastAPI(title=settings.app_name)

app.include_router(router)

@app.get("/")
def root():
    return {"app": settings.app_name, "status": "ok"}

@app.get("/health")
def health():
    return {"status": "ok"}