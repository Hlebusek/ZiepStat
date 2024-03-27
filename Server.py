from DB_Manager import DBM
from fastapi import FastAPI
import datetime


DataBaseManager = DBM()
server = FastAPI()


@server.post("/commit")
async def commitrecord(action: str):
    # Iegūstam datumu un laiku
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()
    return DataBaseManager.WriteTable(current_date,current_time,action)