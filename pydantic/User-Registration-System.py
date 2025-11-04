from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional, Literal
from uuid import UUID, uuid4
from datetime import datetime
import re


class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=20, pattern=r"^[A-Za-z0-9_]+$")
    email: EmailStr
    full_name: Optional[str] = Field(default=None, min_length=3)
    age: int = Field(ge=13)  # >=
    country: Literal["India", "USA", "UK", "Canada"]

    @field_validator("email")
    def lowercase_email(cls, v):
        return v.lower()

    @field_validator("username")
    def no_spaces(cls, v):
        if " " in v:
            raise ValueError("Username must not contain spaces")
        return v


class UserCreate(UserBase):
    password: str

    @field_validator("password")
    def validate_password(cls, v):
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,20}$", v):
            raise ValueError(
                "Password must be 8–20 chars, include upper, lower, and number"
            )
        return v


class UserOut(UserBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    print(id, created_at)


data = {
    "username": "Jayanta_123",
    "email": "TEST@IITG.AC.IN",
    "age": 21,
    "country": "India",
    "password": "StrongPass1",
}

u = UserOut(**data)
