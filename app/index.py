from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import hashlib
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.responses import JSONResponse

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


@app.get("/generate_file")
async def generate_file():
    # Read the content of the existing file
    file_path = "./app/random_text_file.txt"
    with open(file_path, "r") as existing_file:
        file_content = existing_file.read()

    # Calculate checksum
    checksum = hashlib.sha256(file_content.encode()).hexdigest()

    # Return JSON response with status code 200
    response_data = {"checksum": checksum, "content": file_content}
    return JSONResponse(content=response_data, status_code=200)