from datetime import datetime
import pydantic
from typing import Optional
from src.models.schemas.base import BaseSchemaModel

class ServiceInCreate(BaseSchemaModel):
    provider_id:int
    name:str
    description:str
    category:str
    location:str
    cover_image:Optional[str] = None
    gallery:Optional[ str] = None
    email:Optional[pydantic.EmailStr] = None
    website:Optional[str] = None
    starting_prices:Optional[str] = None


class ServiceInUpdate(BaseSchemaModel):
    name:Optional[str] = None
    description:Optional[str] = None
    category:Optional[str] = None
    location:Optional[str] = None
    cover_image:Optional[str] = None
    gallery:Optional[ str] = None
    email:Optional[pydantic.EmailStr] = None
    website:Optional[str] = None
    starting_prices:Optional[str] = None
    is_available:Optional[bool] = None

class ServiceInResponse(BaseSchemaModel):
    id:int
    provider_id:int
    name:str
    description:str | None
    category:str
    location:str
    cover_image:str | None
    gallery: str | None
    email:pydantic.EmailStr | None
    website:str | None
    starting_prices:str | None
    created_at:datetime
    updated_at:datetime | None
    is_available:bool

