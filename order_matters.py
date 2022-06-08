from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_users_me():
    return {"username": "the_current_user"}

@app.get("/users/me")
async def read_users_me():
    return {"username": "the_current_user"}