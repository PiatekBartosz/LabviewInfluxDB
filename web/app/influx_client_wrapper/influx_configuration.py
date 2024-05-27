import os


class InfluxConfiguration:
    INFLUX_BUCKET = os.environ["INFLUXDB_BUCKET"]
    INFLUX_TOKEN = os.environ["INFLUXDB_API_TOKEN"]
    INFLUX_ORG = os.environ["INFLUXDB_ORGANIZATION"]
    INFLUX_URL = os.environ["INFLUXDB_URL"]
