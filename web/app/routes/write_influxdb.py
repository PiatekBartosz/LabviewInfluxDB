from fastapi import APIRouter, Request
# from fastapi.response import JSONResponse
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
        url=InfluxConfiguration.INFLUX_URL
    )

    try:
        for measurement in body.Array:
            t0 = measurement.t0
            dt = measurement.dt
            y_values = measurement.y

            points = []


            await client.record_timeseries(
                measurement=1111,
                timestamp=,
                city,
                country: str,
                card_id: int
            )
    except Exception as e:
        raise e

    # failure_response =
    print(str(labviewData.json()))

    return await None
