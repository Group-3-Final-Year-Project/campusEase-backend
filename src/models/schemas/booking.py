from src.models.schemas.base import BaseSchemaModel
from datetime import datetime
from typing import Optional


class BookingInCreate(BaseSchemaModel):
    service_id:int
    provider_id:int
    user_id:int
    scheduled_service_date:datetime
    service_cost:float
    payment_method:str
    service_address:str
    booking_details:Optional[str] = None
    booking_attachments:Optional[str] = None

class BookingInUpdate(BaseSchemaModel):
    scheduled_service_date:Optional[datetime] = None
    service_cost:Optional[float] = None
    payment_method:Optional[str] = None
    service_address:Optional[str] = None
    booking_details:Optional[str] = None
    booking_attachments:Optional[str] = None

class BookingInResponse(BaseSchemaModel):
    id:int
    service_id:int
    provider_id:int
    user_id:int
    scheduled_service_date:datetime
    service_cost:float
    payment_method:str
    service_address:str
    booking_details:Optional[str] = None
    booking_attachments:Optional[str] = None
    booking_date:datetime
