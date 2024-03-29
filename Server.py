from DB_Manager import DBM
from fastapi import FastAPI
import datetime


DataBaseManager = DBM()
server = FastAPI()


@server.get("/commit")
async def commitrecord(action: str):
    current_datetime = str(datetime.datetime.now())
    return DataBaseManager.WriteTable(current_datetime,action)