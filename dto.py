
import datetime
from typing import List
from pydantic import BaseModel, ConfigDict

from model import UserChat

class Request(BaseModel):
    query: str

class ChatResponse(BaseModel):
    query: str
    response: str
    user_id: int

class ChatHistory(BaseModel):
    query: str
    response: str
    recorded_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)

class History(BaseModel):
    chats: List[ChatHistory]

    model_config = ConfigDict(from_attributes=True)


class User(BaseModel):
    name: str
    email:str
    password:str