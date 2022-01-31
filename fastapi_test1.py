# FastAPI is a Python class that provides all the functionality for your API. FastAPI is a class that inherits directly from Starlette.

from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel

# Here the app variable will be an "instance" of the class FastAPI. This will be the main point of interaction to create all your API.
app  = FastAPI()

class posts(BaseModel):
    title : str
    content : str
    published : bool = True # setting default value
    rating : Optional[int] = None

# The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to the path '/' using a get operation
@app.get('/')
async def root():
    return {"message": "Hello, world!"}

# Path with parameter
@app.get('/items/{item_id}')
async def read_item(item_id):
    return {"item": item_id}

# Path parameters with types
@app.get('/users/{user_id}')
async def read_item(user_id: int):
    return {"user": user_id}

@app.post('/createposts')
def create_post(payload: dict=Body(...)):
    print(payload)
    return {"message": "successfully created post!"}

# using pydantic
@app.post('/createposts2')
def create_post(payload: posts):
    print(payload.published)
    print(payload.rating)
    return {"message": "successfully created post!"}




