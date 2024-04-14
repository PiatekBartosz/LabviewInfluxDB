from pydantic_settings import BaseSettings
from pydantic import SecretStr
import os

# class Settings(BaseSettings):
#     # Influx settings will be stored in envinronmental variables 
#     influx_api_url: str = os.environ.get("INFLUXDB_API_URL")
#     # Store API token (key) 
#     influx_api_token: SecretStr = os.environ.get("INFLUXDB_API_TOKEN")
#     influx_api_orgainzation: str = os.environ.get("INFLUX_API_ORGANIZATION")
