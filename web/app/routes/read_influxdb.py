from fastapi import APIRouter

read_router = APIRouter()

@read_router.get("/read_api", tags=["read_api"])
async def read_api():
    return {"test": "test from read api"}
