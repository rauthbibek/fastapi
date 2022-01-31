from fastapi import FastAPI

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
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return {'items':items_list}