from DB_Manager import DBM
from fastapi import FastAPI

DataBaseManager = DBM()
server = FastAPI()


@server.post("/commit")
async def commitrecord(date: str, time: str, action: str):
    return DataBaseManager.WriteTable(date,time,action)