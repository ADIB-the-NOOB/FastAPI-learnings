from fastapi import FastAPI 

app = FastAPI()

# reading item id from url
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# reading item id(It's Int) from url
@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}