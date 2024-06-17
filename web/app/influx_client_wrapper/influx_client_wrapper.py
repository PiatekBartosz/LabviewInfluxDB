from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.rest import ApiException
from pydantic import SecretStr
from app.influx_client_wrapper.influx_exceptions import EXCEPTION_MAPPING, UnknownException
from collections.abc import Iterable


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
        # TODO secret pass token
        print("variables: ")
        print(" url: ", url, " ", " token: ", token, " org: ", org)
        self._client = InfluxDBClient(
            url="172.16.0.3:8086", token=token, org=self._org)
        self.write_api = None

    def record_timeseries(self, measurement: float, timestamp: str, city: str, country: str, card_id: str) -> None:
        self.write_api = self._client.write_api(write_options=SYNCHRONOUS)
        point = (
            Point("labview_measurement")
            .tag("city", city)
            .tag("country", country)
            .tag("card_id", card_id)
            .field("voltage_V", float(measurement))
            .time(timestamp)
        )
        print("point: ", point)
        self._write_data(point)

    def _write_data(self, point: Point):
        ret = self.write_api.write(bucket=self._bucket,
                                   org=self._org, record=point)
        return ret
