from pydantic_settings import BaseSettings
from pydantic import SecretStr
import os

class Configuration(BaseSettings):
    influxdb_url: str = os.environ.get("INFLUXDB_URL")
    influxdb_token: SecretStr = os.envon.get("INFLUXDB_API_TOKEN")
    influxdb_organization: str = os.environ.get("INFLUXDB_ORGANIZATION")
