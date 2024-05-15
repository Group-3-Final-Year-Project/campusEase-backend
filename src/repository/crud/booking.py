import typing
import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.booking import Booking
from src.models.schemas.booking import BookingInCreate,BookingInUpdate
from src.repository.crud.base import BaseCRUDRepository

class BookingCRUDRepository(BaseCRUDRepository):
    async def create_booking(self,booking_create:BookingCreate) -> Booking:
        # new_booking = Booking()
        pass

    async def read_bookings(self) -> typing.Sequence[Booking]:
        pass

    async def read_booking_by_id(self,id:str) -> Booking:
        pass

    async def update_booking_by_id(self,id:str,booking_update:BookingInUpdate) -> Booking:
        pass

    async def delete_booking_by_id(self,id:str) -> str:
        pass