from fastapi import FastAPI, APIRouter, Request, HTTPException
from models.good import User, UserProfile

# Создаем основной объект FastAPI
app = FastAPI()

users = [
    User(id=1, name="User 1", email="user1@gmail.com"),
    User(id=2, name="User 2", email="user2@mail.com"),
]

users_profile = [
    UserProfile(user_id=1, address="Строителей 23", phone_number="8929356455"),
    UserProfile(user_id=2, address="Строителей 26", phone_number="8929354551")
]

# Создаем объект APIRouter для работы с пользователями
users_router = APIRouter(
    prefix="/users",
    tags=["users"],
)

# Создаем методы для работы с пользователями

# чтение информации о пользователе по его id
@users_router.get("/{user_id}")
async def read_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if user:
        return user.dict()
    else:
        return {"message": "User not found"}

# cоздание информации о новом пользователе
@users_router.post("/")
async def create_user(user: User):
    users.append(user)
    return user.dict()

# изменение информации о пользователе
@users_router.put("/{user_id}")
async def update_user(user_id: int, user: User):
    for u in users:
        if u.id == user_id:
            u.name = user.name
            u.email = user.email
            return u.dict()
    raise HTTPException(status_code=404, detail="User not found")

# удаление информации о пользователе по id
@users_router.delete("/{user_id}")
async def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u.id == user_id:
            del users[i]
            return {"message": f"User with id {user_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

# Создаем методы для работы с профилем пользователя

# чтение профиля пользователя по id
@users_router.get("/{user_id}/profile")
async def read_user_profile(user_id: int):
    user_profile = next((u for u in users_profile if u.user_id == user_id), None)
    if user_profile:
        return user_profile.dict()
    else:
        return {"message": "User not found"}

# создание профиля пользователя
@users_router.post("/{user_id}/profile")
async def create_user_profile(user_id: int, profile: UserProfile):
    profile.user_id = user_id
    users_profile.append(profile)
    return profile.dict()

# изменение профиля пользователя
@users_router.put("/{user_id}/profile")
async def update_user_profile(user_id: int, profile: UserProfile):
    for p in users_profile:
        if p.user_id == user_id:
            p.address = profile.address
            p.phone_number = profile.phone_number
            return p.dict()
    raise HTTPException(status_code=404, detail="User not found")

@users_router.delete("/{user_id}/profile")
async def delete_user_profile(user_id: int):
    for i, p in enumerate(users_profile):
        if p.user_id == user_id:
            del users_profile[i]
            return {"message": f"Profile for user with id {user_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

# Подключаем маршруты для работы с пользователями к приложению
app.include_router(users_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)