from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from db import Base

class UserChat(Base):
    __tablename__ = "userchats"
    
    id= Column(Integer, primary_key=True)
    query= Column(String)
    response= Column(String)
    recorded_at= Column(DateTime, default=datetime.now)