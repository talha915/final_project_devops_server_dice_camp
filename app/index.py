from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

item_list = []

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float
    tax: float    

@app.post("/items/")
def create_item(item: Item):
    item_list.append(item.dict())
    return item.dict()

@app.get("/items/{item_id}")
def search_item(item_id: int):
    searched_items = [item for item in item_list if item.get('id')==item_id]
    searched_items = searched_items if len(searched_items) > 0 else 'Not found'
    return {"result": searched_items}