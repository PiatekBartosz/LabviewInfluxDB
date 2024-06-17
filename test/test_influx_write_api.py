import influxdb_client
import os
import time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "00ONRY_GQCU1O2rqhYVjXMZgwjbVRVSEBSTKGfYbdGsrvfez62Qxac4aCOWurgdYQIRrCZHQTpDXZ_wJy-1A3Q=="
org = "labview"
url = "172.16.0.3:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket = "labview"

write_api = write_client.write_api(write_options=SYNCHRONOUS)

for value in range(5):
    point = (
        Point("measurement1")
        .tag("tagname1", "tagvalue1")
        .field("field1", value)
    )
    write_api.write(bucket=bucket, org="labview", record=point)
    time.sleep(1)  # separate points by 1 second
