import imp
from utils import to_dict
from respuesta import Respuesta

from sqlalchemy.orm import Session
import schema
from session import SessionLocal, engine

#FastAPI
from fastapi import FastAPI, status
from fastapi import Body

schema.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get(
    path = "/",
    status_code=status.HTTP_200_OK,
    tags = ['Home']
)
def home():
    return {"Hello": "World"}

@app.post(
    path = "/",
    status_code=status.HTTP_200_OK,
    tags = ['Home']
)
async def home(res: str = Body(...)):
    response = to_dict(res)
    print(response)
    if Respuesta(response) != None:
        return {"reply": Respuesta(response)}