from fastapi import APIRouter

write_router = APIRouter()

@write_router.get("/write_api", tags=["write_api"])
async def write_api():
    return {"test": "test from write api"}


