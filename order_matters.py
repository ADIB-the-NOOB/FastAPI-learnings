from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_users_me():
    return {"username": "the_current_user"}

@app.get("/users/{user_id}")
async def read_users(user_id: int):
    return {"user_id": user_id}