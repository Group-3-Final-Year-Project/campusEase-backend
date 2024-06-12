import typing
import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.booking import Booking
from src.models.schemas.booking import BookingInCreate,BookingInUpdate
from src.repository.crud.base import BaseCRUDRepository
from src.utilities.exceptions.database import EntityAlreadyExists, EntityDoesNotExist

class BookingCRUDRepository(BaseCRUDRepository):
    async def create_booking(self,booking_create:BookingInCreate) -> Booking:
        new_booking = Booking(**booking_create)
        self.async_session.add(instance=new_booking)
        await self.async_session.commit()
        await self.async_session.refresh(instance=new_booking)
        

    async def read_bookings(self) -> typing.Sequence[Booking]:
        stmt = sqlalchemy.select(Booking)
        query = await self.async_session.execute(statement=stmt)
        return query.scalars().all()

    async def read_booking_by_id(self,id:int) -> Booking:
        stmt = sqlalchemy.select(Booking).where(Booking.id == id)
        query = await self.async_session.execute(statement=stmt)

        if not query:
            raise EntityDoesNotExist(f"Booking with id `{id}` does not exist!")
        return query.scalar()

    async def read_bookings_by_provider_id(self,provider_id:int) -> typing.Sequence[Booking]:
        stmt = sqlalchemy.select(Booking).where(Booking.provider_id == provider_id)
        query = await self.async_session.execute(statement=stmt)

        if not query:
            raise EntityDoesNotExist(f"Bookings with provider id `{provider_id}` does not exist!") 
        
        return query.scalars().all()

    async def read_bookings_by_user_id(self,user_id:int) -> typing.Sequence[Booking]:
        stmt = sqlalchemy.select(Booking).where(Booking.user_id == user_id)
        query = await self.async_session.execute(statement=stmt)

        if not query:
            raise EntityDoesNotExist(f"Bookings with user id `{user_id}` does not exist!") 
        
        return query.scalars().all()

    async def update_booking_by_id(self,id:str,booking_update:BookingInUpdate) -> Booking:
        new_booking_data = booking_update.dict()
        select_stmt = sqlalchemy.select(Booking).where(Booking.id == id)
        query = await self.async_session.execute(statement=select_stmt)
        update_booking = query.scalar()

        if not update_account:
            raise EntityDoesNotExist(f"Booking with id `{id}` does not exist!")

        update_stmt = sqlalchemy.update(table=Booking).where(Booking.id == update_booking.id).values(updated_at=sqlalchemy_functions.now(),**new_booking_data)

        await self.async_session.execute(statement=update_stmt)
        await self.async_session.commit()
        await self.async_session.refresh(instance=update_booking)

        return update_booking


    async def delete_booking_by_id(self,id:str) -> str:
        select_stmt = sqlalchemy.select(Booking).where(Booking.id == id)
        query = await self.async_session.execute(statement=select_stmt)
        delete_account = query.scalar()

        if not delete_account:
            raise EntityDoesNotExist(f"Booking with id `{id}` does not exist!")  # type: ignore

        stmt = sqlalchemy.delete(table=Booking).where(Booking.id == delete_account.id)

        await self.async_session.execute(statement=stmt)
        await self.async_session.commit()

        return f"Booking with id '{id}' is successfully deleted!"
