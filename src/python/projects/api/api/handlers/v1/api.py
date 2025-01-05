from api.core import security
from fastapi import APIRouter, Depends
from . import document, analyze
api_router = APIRouter()
api_router.include_router(
    document.router, prefix="/document", tags=["document"], dependencies=[Depends(security.verify_http_auth_basic)]
)
api_router.include_router(
    analyze.router, prefix="/analyze", tags=["analyze"], dependencies=[Depends(security.verify_http_auth_basic)]
)
