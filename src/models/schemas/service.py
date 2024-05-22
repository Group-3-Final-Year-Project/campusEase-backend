from datetime import datetime
import pydantic
import json
from src.models.schemas.base import BaseSchemaModel

class ServiceInCreate(BaseSchemaModel):
    id:str
    provider_id:str
    name:str
    description:str
    category:str
    location:str
    cover_image:str | None
    gallery: str | None
    email:pydantic.EmailStr | None
    website:str | None
    starting_prices:str | None


class ServiceInUpdate(BaseSchemaModel):
    id:str
    provider_id:str
    name:str
    description:str
    category:str
    location:str
    cover_image:str | None
    gallery: str | None
    email:pydantic.EmailStr | None
    website:str | None
    starting_prices:str | None
    is_available:bool

class ServiceInResponse(BaseSchemaModel):
    id:str
    provider_id:str
    name:str
    description:str
    category:str
    location:str
    cover_image:str | None
    gallery: str | None
    email:pydantic.EmailStr | None
    website:str | None
    starting_prices:str | None
    created_at:datetime
    updated_at:datetime
    is_available:bool

