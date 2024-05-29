import datetime
from typing import Optional
import pydantic

from src.models.schemas.base import BaseSchemaModel


class AccountInCreate(BaseSchemaModel):
    username: str
    email: pydantic.EmailStr
    phone_number:str
    password: str
    user_type:str



class AccountInUpdate(BaseSchemaModel):
    username: Optional[str] = None
    email: Optional[pydantic.EmailStr] = None
    phone_number: Optional[str] = None
    password: Optional[str] = None
    user_type: Optional[str] = None
    location: Optional[str] = None
    profile_picture: Optional[str] = None
    is_email_verified: Optional[bool] = None
    is_phone_verified: Optional[bool] = None
    is_active: Optional[bool] = None
    is_logged_in: Optional[bool] = None



class AccountInLogin(BaseSchemaModel):
    username: str
    email: pydantic.EmailStr
    password: str


class AccountWithToken(BaseSchemaModel):
    token: str
    username: str
    email: pydantic.EmailStr
    phone_number:str | None
    user_type:str
    location:str | None
    profile_picture:str | None
    is_email_verified: bool
    is_phone_verified: bool
    is_active: bool
    is_logged_in: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime | None


class AccountInResponse(BaseSchemaModel):
    id: int
    authorized_account: AccountWithToken


class AccountOTP(BaseSchemaModel):
    otp:str

