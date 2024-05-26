from fastapi import APIRouter, Request
from fastapi.response import JSONResponse
from influx_client_wrapper.influx_client_wrapper import InfluxClientWrapper
from influx_client_wrapper.influx_configuration import InfluxConfiguration

write_router = APIRouter()


@write_router.get("/write_api", tags=["write_api"])
async def write_api():
    return {"test": "test from write api"}


@write_router.post("/write_api", tags=["write_api"])
async def write_api_post(labviewData: Request):
    # log incoming data
    request_data = await labviewData

    body = request_data.body()
    json_str = body.decode('utf-8')
    print("From labview: ", json_str)

    request_json = request_data.json()
    client = InfluxClientWrapper(
        bucket=InfluxConfiguration.INFLUX_BUCKET,
        org=InfluxConfiguration.INFLUX_ORG,
        token=InfluxConfiguration.INFLUX_TOKEN
    )

    try:
        await client.record_timeseries(
            measurement=)

    sucess_respose =

    failure_response =

    return await str(labviewData.json())
