from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from pydantic import SecretStr
from typing import Any
from datetime import datetime


class InfluxWaveClient:
    """
        This client uses influxdb_client as dependency injection
    """
    MEASUREMENT_NAME: str = "daq_measurements"

    def __init__(self, bucket: str, token: SecretStr, org: str, url: str) -> None:
        self.bucket = bucket
        self._client = InfluxDBClient(
            url=url, token=token.get_secret_value(), org=org)

    async def record_daq_measurement(self, daq_number: int, value: float) -> None:
        point = (
            Point(InfluxWaveClient.MEASUREMENT_NAME)
            .tag("daq_number", daq_number)
            .value("value", value)
        )
        point = Point("my_measurement").tag("daq_number", daq_number).field(
            "voltage_value", value).time(datetime.now(), write_precision=datetime.WritePrecision.MS)
        await self._insert(point)

    async def read_daq_measurement(self, daq_number: int, value: float):
        pass

    async def _insert(self, point: Point) -> Any:
        write_api = self._client.write_api(write_options=SYNCHRONOUS)
        try:
            ret = write_api.write(bucket=self.bucket, record=point)
        # TODO: custom errors?
        except Exception as e:
            raise e
        # TODO: log error
        return ret

    async def _query(self, point: Point) -> Any:
        # TOOD: handle influxdb query
        pass
