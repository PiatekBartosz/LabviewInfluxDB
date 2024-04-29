from pydantic import BaseModel, Field

class DaqMeasurement_insert_request(BaseModel):
    value: float = Field(description="Measurement value")
    daq_number: int = Field(description="Number of the DAQ card")


