from fastapi import FastAPI
from app.routes.beers_router import beers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuracion del CORS en los encabezados
origin = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(beers)