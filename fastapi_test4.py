from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Items(BaseModel):
    name: str
    price: float
    description: Optional[str]= None
    tax: Optional[float]= None


app = FastAPI()

# Pydantic type validation
@app.post('/items/')
async def create_items(item: Items):
    print(item)
    return item