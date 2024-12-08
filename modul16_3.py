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
async def create_user(username:str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
                      age:int = Path(ge=18, le=120, description='Enter age', example='77')) -> dict:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                     example="UrbanUser")],
                       user_id: str = Path(ge=1, le=100, description="Enter User ID", example="25"),
                       age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete('/user/{user_id}')
async def del_user(user_id: str = Path(ge=1, le=100, description="Enter User ID", example="25"),) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users.pop(user_id)
    return f"User {user_id} was deleted."



