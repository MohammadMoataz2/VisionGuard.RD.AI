from api.core import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from . import models

class DBEngine:
    def __init__(self) -> None:
        self._client: AsyncIOMotorClient = None

    @property
    def client(self) -> AsyncIOMotorClient:
        return self._client

    async def connect(self):
        print(settings)
        self._client: AsyncIOMotorClient = AsyncIOMotorClient(
            settings.DB_CONN_STRING, maxPoolSize=settings.DB_MAX_CONNECTIONS, minPoolSize=settings.DB_MIN_CONNECTIONS
        )
        print(models.beanie_models)

        await init_beanie(database=self._client[settings.DB_NAME], document_models=models.beanie_models)

    async def close(self):
        self._client.close()


db_engine = DBEngine()

