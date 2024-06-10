from pydantic import BaseModel, Field
from fastapi import APIRouter, Request, Body
# from fastapi.response import JSONResponse
from app.influx_client_wrapper.influx_client_wrapper import InfluxClientWrapper
from app.influx_client_wrapper.influx_configuration import InfluxConfiguration
from typing import Any
from datetime import datetime, timedelta
import time

write_router = APIRouter()

# TODO only for tests


class InsertResponse(BaseModel):
    bucket: str = Field()
    location: str = Field()
    height: str = Field()


@write_router.get("/write_api", tags=["write_api"])
async def write_api():
    return {"test": "test from write api"}


@write_router.post("/write_api", tags=["write_api"])
def write_api_post(payload: Any = Body(None)):

    body = payload

    client = InfluxClientWrapper(
        bucket=InfluxConfiguration.INFLUX_BUCKET,
        org=InfluxConfiguration.INFLUX_ORG,
        token=InfluxConfiguration.INFLUX_TOKEN,
        url=InfluxConfiguration.INFLUX_URL
    )

    try:
        dict_mesurement = body["Array"][0]
        t0 = dict_mesurement["t0"]
        dt = dict_mesurement["dt"]
        city = payload["City"]
        country = payload["Country"]
        card_id = payload["CardId"]

        print("Test write data:")
        print("array = ", dict_mesurement)
        print("to = ", t0, "type= ", type(t0))
        print("dt = ", dt, "type= ", type(dt))
        print("city = ", city)
        print("country = ", country)
        print("card_id = ", card_id)

        t0 = datetime.fromisoformat(t0.replace('Z', '+00:00'))
        dt = timedelta(seconds=dt)

        for i, measurement in enumerate(dict_mesurement['y']):
            timestamp = t0 + i * dt
            timestamp_string = timestamp.isoformat().replace('+00:00', 'Z')
            print("timestamp_string: ", timestamp_string)
            client.record_timeseries(
                measurement=measurement,
                timestamp=timestamp_string,
                city=city,
                country=country,
                card_id=str(card_id)
            )

    except Exception as e:
        raise e

    # return InsertResponse(bucket="fdsaf", location="fjdasf", height="fdsafads")
    return payload
