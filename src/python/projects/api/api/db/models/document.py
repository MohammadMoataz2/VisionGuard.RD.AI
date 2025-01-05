from beanie import Document as Model
from beanie import PydanticObjectId
from pydantic import BaseModel, Field
from api.api_interface.v1.schema import SearchEngineUser,Ad


class DocumentDBBase(SearchEngineUser, Model):

    class Settings:
        name = "user2"

class AdDBBaese(Ad, Model):
    class Settings:
        name = "ads_collection"

Document = DocumentDBBase
User_Ad = AdDBBaese