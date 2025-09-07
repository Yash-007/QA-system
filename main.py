from fastapi import Depends, FastAPI, HTTPException, Header
from dotenv import load_dotenv
from sqlalchemy import exc
from sqlalchemy.orm import Session
from db import SessionLocal, engine
from dto import ChatResponse, History, Request, User
from llm import ask_query
import model
import repo

model.Base.metadata.create_all(bind = engine)

app = FastAPI()
load_dotenv()


def get_db():
    db = SessionLocal()
    try:
        yield db
        print("connected to db")
    finally:
        db.close()

def get_user(x_user_id: int = Header(...)):
    print(x_user_id)
    if x_user_id != 1:
        raise HTTPException(
        status_code=401,
        detail="Unauthorized user"
    )
    return x_user_id

@app.post("/register")
def register_user(user: User, db:Session=Depends(get_db)):
    try:
       user= repo.create_user(db, user)
       return user

    except Exception as e:
        print(f"got the error: {e}")
        return HTTPException(
            status_code=500,
            detail="Internal server error"
        )

@app.post("/ask")
def ask_llm(data: Request, user_id: int = Depends(get_user), db: Session = Depends(get_db)):
    try:
            response = ask_query(data.query)
            if response:
                repo.SaveUserData(db, user_id, data.query, response)
                return ChatResponse(
                    user_id=user_id,
                    query=data.query,
                    response=response
                )

    except Exception as e:
        print("got the error: ", e)
        return HTTPException(
                status_code=500,
                detail="Internal Server Error"
        )

@app.get("/history", response_model= History)
def get_user_history(user_id: int = Depends(get_user), db: Session = Depends(get_db)):
    chats = repo.GetUserChats(db, user_id)
    return History(
        chats=chats
    )


    

