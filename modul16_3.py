from fastapi import FastAPI, Path
from typing import Annotated

    # Создаем экземпляр приложения FastAPI
app = FastAPI()
    # Создайте словарь users
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/")
async def start_page() -> dict:
    return {"message": "Главная страница"}
    # 4 CRUD запроса:
@app.get('/users')
async def get_message() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete('/user/{user_id}')
async def del_user(user_id: str) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users.pop(user_id)
    return f"User {user_id} was deleted."

