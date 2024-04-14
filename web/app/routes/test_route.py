from fastapi import APIRouter
import os

test_router = APIRouter()

@test_router.get("/env", tags=["env"])
async def test_env():
    env_variables = {}
    env_variables["USER"]= os.environ.get("INFLUXDB_USER")
    env_variables["PASSWORD"]= os.environ.get("INFLUXDB_PASSWORD")
    env_variables["ORGANIZATION"]= os.environ.get("INFLUXDB_ORGANIZATION")
    env_variables["BUCKET"]= os.environ.get("INFLUXDB_BUCKET")
    env_variables["API_TOKEN"]= os.environ.get("INFLUXDB_API_TOKEN")
    return {"Environmental variables": env_variables}