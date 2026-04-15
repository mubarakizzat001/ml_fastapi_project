
from fastapi import FastAPI
from contextlib import asynccontextmanager
from scalar_fastapi import get_scalar_api_reference
from database.seesion import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)




@app.get("/scalar",include_in_schema=False)
def scalar_api():
    return get_scalar_api_reference(
        openapi_url= app.openapi_url,
        title="ML Model API"
    )

