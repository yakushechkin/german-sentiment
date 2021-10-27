from typing import List
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class SentimentRequest(BaseModel):
    texts: List[str]


class SentimentResponse(BaseModel):
    sentiments: List[str]
