import sys
from fastapi import Depends, FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.responses import JSONResponse
from api.core import settings
from api.core import security
from api.core.logger import setup_logger

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import redis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
logger = setup_logger()

logger.warning("FastAPI starting!")



app = FastAPI(
    title=settings.api_app_name,
    version=settings.app_version,
    docs_url=None,
    redoc_url=None,
)


from .db import db_engine

@app.on_event("startup")
async def on_startup():
    redis_client = redis.from_url("redis://localhost", encoding="utf8")
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")

    if settings.DB_INIT_DURING_STARTUP:
        await db_engine.connect()

@app.on_event("shutdown")
async def on_shutdown():
    await db_engine.close()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    logger.error(f"{request}: {exc_str}")
    content = {"status_code": 10422, "message": exc_str, "data": None}
    return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@app.get("/", tags=[""])
def read_root():
    return {"Vision": "Guard"}


from .handlers import v1

app.include_router(v1.api_router, prefix=settings.API_V_STR)



@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(
    username: str = Depends(security.verify_http_auth_basic) if settings.USE_DOC_AUTH else "",
):
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title,
    )


@app.get("/redoc", include_in_schema=False)
async def redoc_html(username: str = Depends(security.verify_http_auth_basic) if settings.USE_DOC_AUTH else ""):
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title,
    )