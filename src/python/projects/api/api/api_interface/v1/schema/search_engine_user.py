from pydantic import BaseModel, Field
from googlesearch import search as bs4search_google
from pydantic_settings import BaseSettings
from uuid import uuid4, UUID
from typing import List
from datetime import datetime as datetimenow
from enum import Enum
from .search_engine_query import SearchEngineQuery, SearchEngineResult



class EmotionEnum(Enum):
    SAD = "sad"
    ANGRY = "angry"
    SURPRISE = "surprise"
    FEAR = "fear"
    HAPPY = "happy"
    DISGUST = "disgust"
    NEUTRAL = "neutral"

class RaceEnum(Enum):
    INDIAN = "indian"
    ASIAN = "asian"
    LATINO_HISPANIC = "latino hispanic"
    BLACK = "black"
    MIDDLE_EASTERN = "middle eastern"
    WHITE = "white"



class GenderEnum(Enum):
    Man =  "Man"
    Woman =  "Woman"

class SearchApproachEnum(str, Enum):
    BS4_GOOGLE = "bs4_google"
    SELENIUM = "selenium"



class SearchEngineUserQuery(BaseSettings):
    query_id: UUID = Field(default_factory=uuid4)
    query_obj : SearchEngineQuery
    datetime: datetimenow = Field(default_factory=datetimenow.now)
    approach: SearchApproachEnum = Field(default=SearchApproachEnum.BS4_GOOGLE)


class SearchEngineResultQuery(BaseModel):
    query_result: List[SearchEngineResult]
    datetime: datetimenow = Field(default_factory=datetimenow.now)


class SearchEngineUserResultQuery(BaseModel):
    user_query: SearchEngineUserQuery = None
    result_query: SearchEngineResultQuery = None

class SearchEngineUserAttribute(BaseModel):
    default_attributes: bool = Field(default=True, description="User's default attributes")
    race : RaceEnum = Field(default="asian", description="User's race")
    gender : GenderEnum = Field(default="Man", description="User's gender")
    age: int = Field(default=0, description="User's age")
    emotion : EmotionEnum = Field(default="neutral", description="User's emotion")


class SearchEngineUserAttributeOther(BaseModel):
    location: str = Field(default = "", description="User's location")


class SearchEngineUser(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    user_name: str = Field(default="<USERNAME>")
    user_email: str = Field(default="<EMAIL>")
    user_password: str = Field(default="<PASSWORD>")
    user_preferences: dict = Field(default_factory=dict)
    created_time: datetimenow = Field(default_factory=datetimenow.now)
    face_path: List[str] = Field(default_factory=list)
    user_attributes: SearchEngineUserAttribute = Field(default_factory=SearchEngineUserAttribute)

    user_attributes_other: SearchEngineUserAttributeOther = Field(default_factory=SearchEngineUserAttributeOther)
    user_query_result: List[SearchEngineUserResultQuery] = Field(default_factory=list)






#sass