from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    email: str


class UserProfile(BaseModel):
    user_id: int
    address: str
    phone_number: str
