from fastapi import APIRouter, Request
from fastapi.response import JSONResponse

write_router = APIRouter()

@write_router.get("/write_api", tags=["write_api"])
async def write_api():
    return {"test": "test from write api"}

@write_router.post("/write_api", tags=["write_api"])
async def write_api_post(labviewData: Request):
    body = await labviewData.body()
    json_str = body.decode('utf-8')
    print("From labview: ", json_str)

    

    sucess_respose = 

    failure_response = 

    return await str(labviewData.json())
