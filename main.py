from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.actor import actor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
)

app.include_router(actor)