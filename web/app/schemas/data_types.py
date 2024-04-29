
from pydantic import BaseModel, Field

class DaqMeasurement(BaseModel):
    daq_number: int = Field(description="Number of the DAQ card")
    value: float = Field(description="Measurement value")
