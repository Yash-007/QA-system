
from typing import List
from pydantic import BaseModel, ConfigDict

from model import UserChat

class Request(BaseModel):
    query: str

class ChatResponse(BaseModel):
    query: str
    response: str

class History(BaseModel):
    status: int
    message: str
    history: List[UserChat]

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)