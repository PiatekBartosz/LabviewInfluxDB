from typing import Union
from fastapi import FastAPI
from app.routes.read_influxdb import read_router
from app.routes.write_influxdb import write_router
from app.routes.test_route import test_router

# test env variables
import os

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Test purposes only
app.include_router(read_router)
app.include_router(write_router)
app.include_router(test_router)
