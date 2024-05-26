from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.rest import ApiException
from pydantic import SecretStr
from influx_client_wrapper.influx_exceptions import EXCEPTION_MAPPING, UnknownException


class InfluxClientWrapper:
    """
    This class is ment ment to be an abstraction and restricted access 
    for InfluxDBClient class implemented as dependency injection pattern.  
    """

    def __init__(self, bucket: str, token: SecretStr, org: str, url: str):
        """Contructor for InfluxDB Client Class

        :param bucket: Defines influx write bucket.
        :type bucket: str
        :param token: Defines API Token Key for influx.
        :type token: SecretStr
        :param org: Defines influx org
        :type org: str
        :param url: Defines influx URL
        :type url: str
        """
        self._org = org
        self._bucket = bucket
        self._client = InfluxDBClient(
            url=url, token=token.get_secret_value(), org=self._org)

    async def record_timeseries(self, measurement: float, timestamp: str, city: str, country: str, card_id: int) -> None:
        point = (
            Point("Labview")
            .tag("city", city.lower())
            .tag("country", country.lower())
            .tag("card_id", card_id)
            .field("voltage_V", measurement)
        )
        await self._write_data(point)

    async def _write_data(self, point: Point):
        write_api = self._client.write_api(write_options=SYNCHRONOUS)
        try:
            ret = write_api(bucket=self._bucket, org=self._org, record=point)
            return ret
        except ApiException as e:
            exception = EXCEPTION_MAPPING.get(e.status, UnknownException)
            raise exception
