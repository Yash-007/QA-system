

from sqlalchemy.orm import Session

import dto
from model import User, UserChat

def create_user(db: Session, user: dto.User):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def SaveUserData(db: Session, user_id:int, query: str, response: str):
    data = UserChat(
        user_id= user_id,
        query = query,
        response= response
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data
    

def GetUserChats(db: Session, user_id: int):
   chats= db.query(UserChat).filter(UserChat.user_id == user_id).all()
   return chats