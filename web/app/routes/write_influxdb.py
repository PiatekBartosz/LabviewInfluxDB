from fastapi import APIRouter

write_router = APIRouter(prefix="/write")


@write_router.post(
    "/{bucket}/insert",
    responses={
        201: {"description": "Successfully Inserted Into Bucket."},
        400: {"description": "Bad data requested."},
        404: {"description": "Bucket not found."},
        503: {"description": "InfluxDB Not Available"},
    }
)
async def insert_bucket()

