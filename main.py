from fastapi import Depends, FastAPI, HTTPException
from dotenv import load_dotenv
from sqlalchemy import exc
from sqlalchemy.orm import Session
from db import SessionLocal, engine
from dto import ChatResponse, Request
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

@app.post("/ask")
def ask_llm(data: Request, db: Session = Depends(get_db)):
    try:
            response = ask_query(data.query)
            if response:
                repo.SaveUserData(db, data.query, response)
                return ChatResponse(
                    query=data.query,
                    response=response
                )

    except Exception as e:
        print("got the error: ", e)
        return HTTPException(
                status_code=500,
                detail="Internal Server Error"
        )

    

