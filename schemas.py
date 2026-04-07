from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class FocusSettingsUpdate(BaseModel):
    mode: Literal["timer", "stopwatch", "pomodoro"]
    duration_minutes: int = Field(ge=10, le=120)
    allowed_apps: list[str] = Field(default_factory=list, max_length=5)


class FocusSettingsRead(BaseModel):
    mode: Literal["timer", "stopwatch", "pomodoro"]
    duration_minutes: int = Field(ge=10, le=120)
    allowed_apps: list[str] = Field(default_factory=list, max_length=5)

    class Config:
        from_attributes = True