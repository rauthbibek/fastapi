from fastapi import FastAPI, Query, Path
from typing import Optional
from pydantic import BaseModel

class Items(BaseModel):
    item_id: int
    item_name: str
    description: Optional[str]= None
    price: int

# item_list = [{'item_id': "abc1",
#         'item_name': "Table",
#         'price': 1200
#     }]
    
app = FastAPI()

# including Path, Query and request body parameters
@app.get('/items/{item_id}')
async def read_items(item_id: int = Path('...', title = 'This is a mandatory field'),
q : Optional[str] = Query(None, max_length=5),
items: Items = None):
    results = {"item_id": item_id}
    if q:
        results.update({'q': q})
    if items:
        results.update({'items': items})
    return results

   
