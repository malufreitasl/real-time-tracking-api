from fastapi import FastAPI
from app.controllers.gateway_controller import router as gateway_router

app = FastAPI()

app.include_router(gateway_router)
