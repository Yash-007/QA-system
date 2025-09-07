from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from db import Base

class User(Base):
    __tablename__ = "users"

    name = Column(String)
    email = Column(String, unique=True)
    id = Column(Integer, unique=True, primary_key=True)
    password = Column(String)

class UserChat(Base):
    __tablename__ = "userchats"
    
    id= Column(Integer, primary_key=True)
    user_id = Column(Integer)
    query= Column(String)
    response= Column(String)
    recorded_at= Column(DateTime, default=datetime.now)