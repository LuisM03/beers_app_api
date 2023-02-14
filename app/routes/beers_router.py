from fastapi import APIRouter
from app.config.client_db import db
from app.schema.beers_schema import beers_schema

beers = APIRouter(
    prefix="/beers",
    tags=["Beers"]
)

@beers.get("/")
async def getAllBeers():
    beers = db.beers.find()
    return beers_schema(beers)
