import pymysql
from dbutils.pooled_db import PooledDB
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)

app = FastAPI()


class AirPollution(BaseModel):
    pm: int
    co: float
    trafficindex: float


@app.get("/air")
def get_pollution() -> list[AirPollution]:
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT pm, co, trafficindex FROM integration
        """)
        result = [AirPollution(pm=pm, co=co, trafficindex=trafficindex) for pm, co, trafficindex in cs.fetchall()]
    return result
