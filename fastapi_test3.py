from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

items_list = [
    {
        "item_name": "table"
    },
    {
        "item_name": "chair"
    },
    {
        "item_name": "bed"
    }
]

# with query parameters
# @app.get("/items")
# def get_items(skip: int = 0, limit: int = 10):
#     return {'items':items_list}

# query parameters with string validations
# @app.get("/items")
# async def read_items(q: Optional[str]=None):
#     items ={"items":{"item id": "abc", "item name": "Table"}}
#     if q is not None:
#         items.update({"q":q})
#     return items

# query parameters with string validations and extra length validations
@app.get("/items")
async def read_items(q: Optional[str]=Query(None, max_length=5)):
    items ={"items":{"item id": "abc", "item name": "Table"}}
    if q is not None:
        items.update({"q":q})
    return items
