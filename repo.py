

from sqlalchemy.orm import Session

from model import UserChat


def SaveUserData(db: Session, query: str, response: str):
    data = UserChat(
        query = query,
        response= response
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    return data
    