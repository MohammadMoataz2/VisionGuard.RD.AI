from pydantic import BaseModel, Field
from googlesearch import search as bs4search_google
from pydantic_settings import BaseSettings
from uuid import uuid4
from typing import List
from datetime import datetime



class SearchEngineResult(BaseModel):
    url: str = Field(default="")
    title: str = Field(default="")
    description: str = Field(default="")
    categories: list = Field(default_factory=list)


class SearchEngineQuery(BaseSettings):
    SEARCH_TERM: str = Field(default="islam")
    SEARCH_TERM_OPTIMIZED: str = Field(default="")
    SEARCH_USER_PREFERENCES: dict = Field(default_factory=dict)
    SEARCH_OPTIMIZED : bool = Field(default=False)
    SEARCH_CATEGORY: list = Field(default_factory=list)
    # attributes_obj : None
    SEARCH_ADVANCED: bool = Field(default=True)
    SEARCH_NUM_RESULTS: int = Field(default=10)
    SEARCH_LANG: str  = "en" # TODO:  Enum Class
    SEARCH_REGION: str  = "" # TODO: Enum Class
    SEARCH_SAFE: bool = True
    SEARCH_SLEEP_INTERVAL: int = 0
    SEARCH_TIMEOUT: int = 5
    SEARCH_PROXY : str = ""
    SEARCH_SSL_VERIFY : str = ""

    # def query_building(self, user: SearchEngineUser) -> str:
    #     pass

    def search(self, query):
        pass

    #
    # class Config:
    #     env_file = ".env"  # Specify the name of the environment file


class SearchEngineQueryBs4Google(SearchEngineQuery):

    def search(self, query=None):
        print(self)

        return [
            SearchEngineResult(
                url=search_result.url,
                title=search_result.title,
                description=search_result.description,
                categories=["default"]

            )
            for search_result in bs4search_google(

                term=self.SEARCH_TERM if self.SEARCH_OPTIMIZED == False else self.SEARCH_TERM_OPTIMIZED,

                num_results=self.SEARCH_NUM_RESULTS,
                lang=self.SEARCH_LANG,
                proxy=self.SEARCH_PROXY,
                advanced=self.SEARCH_ADVANCED,
                sleep_interval=self.SEARCH_SLEEP_INTERVAL,
                timeout=self.SEARCH_TIMEOUT,
                safe=self.SEARCH_SAFE,
                ssl_verify=self.SEARCH_SSL_VERIFY,
                region=self.SEARCH_REGION

            )
        ]

