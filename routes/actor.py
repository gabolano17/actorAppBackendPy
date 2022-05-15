from fastapi import APIRouter
from config.db import conn
from models.Actor import actors

actor = APIRouter()

@actor.get("/actor/listar")
def getActors():
    return conn.execute(actors.select()).fetchall()

@actor.get("/actor/listar/{id}")
def getActorsId(id: int):
    return conn.execute(actors.select().where(actors.c.actor_id == id)).first()