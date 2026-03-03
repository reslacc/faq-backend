from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="FAQ Backend API",
    version="1.0.0"
)
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)