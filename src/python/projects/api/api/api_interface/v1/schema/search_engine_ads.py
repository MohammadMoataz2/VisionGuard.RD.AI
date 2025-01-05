from beanie import Document
from pydantic import BaseModel
from typing import List, Union, Optional


class AgeRange(BaseModel):
    min: int
    max: int


class AdContent(BaseModel):
    type: str
    url: str


class AttributesTargeting(BaseModel):
    age_range: Optional[AgeRange] = None
    gender: Optional[List[str]] = None
    race: Optional[List[str]] = None
    emotion: Optional[List[str]] = None

class Ad(BaseModel):
    ad_title: str
    category: List[str]
    ad_content: AdContent
    attributes_targeting: Optional[AttributesTargeting] = None  # Make this optional
    location_targeting: Optional[List[str]] = None
    priority: Optional[int] = None  # Make priority optional
