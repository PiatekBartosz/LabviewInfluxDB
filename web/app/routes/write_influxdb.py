from pydantic import BaseModel, Field
from fastapi import APIRouter, Request, Body
# from fastapi.response import JSONResponse
from app.influx_client_wrapper.influx_client_wrapper import InfluxClientWrapper
from app.influx_client_wrapper.influx_configuration import InfluxConfiguration
from typing import Any

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
async def write_api_post(payload: Any = Body(None)):

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
        measurement = dict_mesurement["y"][0]
        city = payload["City"]
        country = payload["Country"]
        card_id = payload["CardId"]

        print("Test write data:")
        print("array = ", dict_mesurement)
        print("to = ", t0)
        print("measurement = ", measurement)
        print("city = ", city)
        print("country = ", country)
        print("card_id = ", card_id)

        await client.record_timeseries(
            measurement=float(measurement),
            timestamp=t0,
            city=city,
            country=country,
            card_id=int(card_id)
        )
    except Exception as e:
        raise e

    # return InsertResponse(bucket="fdsaf", location="fjdasf", height="fdsafads")
    return payload
