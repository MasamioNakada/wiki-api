from utils import to_dict
from respuesta import Respuesta

#FastAPI
from fastapi import FastAPI, status
from fastapi import Body

app = FastAPI()

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