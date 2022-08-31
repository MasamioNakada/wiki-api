from utils import to_dict

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
async def home(
    res: str = Body(...),
):
    response = to_dict(res)
    return {"reply": response["app"]}