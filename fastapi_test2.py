# FastAPI is a Python class that provides all the functionality for your API. FastAPI is a class that inherits directly from Starlette.

from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel

# Here the app variable will be an "instance" of the class FastAPI. This will be the main point of interaction to create all your API.
app  = FastAPI()

my_posts = [{"title":"Post no. 1",
            "content": "Content for post 1",
            "id":1},{"title":"Post no. 2",
            "content": "Content for post 2",
            "id":2}]

class posts(BaseModel):
    title : str
    content : str
    id: int
    published : bool = True # setting default value
    rating : Optional[int] = None

# The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to the path '/' using a get operation
@app.get('/')
async def root():
    return {"message": "Hello, world!"}

@app.get('/posts')
def read_post():
    return {"posts": my_posts}

@app.get('/posts/{id}')
def read_post(id: int):
    for post in my_posts:
        #print(post)
        if post["id"] == id:
            return post

# @app.post('/createposts')
# def create_post(payload: dict=Body(...)):
#     print(payload)
#     return {"message": "successfully created post!"}

# # using pydantic
# @app.post('/createposts2')
# def create_post(payload: posts):
#     print(payload.published)
#     print(payload.rating)
#     return {"message": "successfully created post!"}

@app.post('/posts')
def create_post(post: posts):
    post = post.dict()
    if post is not None:
        my_posts.append(post)
    return post



