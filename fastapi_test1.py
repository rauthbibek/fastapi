# FastAPI is a Python class that provides all the functionality for your API. FastAPI is a class that inherits directly from Starlette.

from fastapi import FastAPI

# Here the app variable will be an "instance" of the class FastAPI. This will be the main point of interaction to create all your API.
app  = FastAPI()

# The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to the path '/' using a get operation
@app.get('/')
async def root():
    return {"message": "Hello, world!"}

