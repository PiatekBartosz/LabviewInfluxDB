from typing import Union
from fastapi import FastAPI
# test env variables
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Test purposes only
@app.get("/env")
def read_root():
    env = {}
    env["url"] = os.environ.get("INFLUXDB_API_URL")
    env["token"] = os.environ.get("INFLUXDB_API_TOKEN")
    env["org"] = os.environ.get("INFLUX_API_ORGANIZATION")
    return env
