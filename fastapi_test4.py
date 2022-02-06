from fastapi import FastAPI, Query, Path
from typing import Optional
from pydantic import BaseModel

# class Items(BaseModel):
#     name: str
#     price: float
#     description: Optional[str]= None
#     tax: Optional[float]= None


app = FastAPI()

# Pydantic type validation
# @app.post('/items/')
# async def create_items(item: Items):
#     print(item)
#     return item

@app.get("/items/{item_id}")
async def read_items(item_id: Path(..., title="Item id need to be passed"),
q: Optional[str]=Query(None, max_length=5)):
    items ={"items":{"item id": item_id, "item name": "Table"}}
    if q is not None:
        items.update({"q":q})
    return items
