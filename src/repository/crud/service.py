import typing
import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.service import Service
from src.models.schemas.service import ServiceInCreate,ServiceInUpdate
from src.repository.crud.base import BaseCRUDRepository
from src.utilities.exceptions.database import EntityAlreadyExists, EntityDoesNotExist

class ServiceCRUDRepository(BaseCRUDRepository):
    async def create_service(self,service_create:ServiceInCreate) -> Service:
        new_service = Service(**(service_create.dict()))
        self.async_session.add(instance=new_service)
        await self.async_session.commit()
        await self.async_session.refresh(instance=new_service)
        return new_service
        

    async def read_services(self) -> typing.Sequence[Service]:
        stmt = sqlalchemy.select(Service)
        query = await self.async_session.execute(statement=stmt)
        return query.scalars().all()

    async def read_service_by_id(self,id:int) -> Service:
        stmt = sqlalchemy.select(Service).where(Service.id == id)
        query = await self.async_session.execute(statement=stmt)

        if not query:
            raise EntityDoesNotExist(f"Service with id `{id}` does not exist!")
        return query.scalar()

    async def read_services_by_name(self,name:str) -> typing.Sequence[Service]:
        stmt = sqlalchemy.select(Service).where(name in Service.name)
        query = await self.async_session.execute(statement=stmt)

        if not query:
            raise EntityDoesNotExist("Services with name `{name}` does not exist!".format(name=name)) 
        
        return query.scalars().all()

    async def update_service_by_id(self,id:str,service_update:ServiceInUpdate) -> Service:
        new_service_data = service_update.dict()
        select_stmt = sqlalchemy.select(Service).where(Service.id == id)
        query = await self.async_session.execute(statement=select_stmt)
        update_service = query.scalar()

        if not update_account:
            raise EntityDoesNotExist(f"Service with id `{id}` does not exist!")

        update_stmt = sqlalchemy.update(table=Service).where(Service.id == update_service.id).values(updated_at=sqlalchemy_functions.now(),**new_service_data)

        await self.async_session.execute(statement=update_stmt)
        await self.async_session.commit()
        await self.async_session.refresh(instance=update_service)

        return update_service


    async def delete_service_by_id(self,id:str) -> str:
        select_stmt = sqlalchemy.select(Service).where(Service.id == id)
        query = await self.async_session.execute(statement=select_stmt)
        delete_account = query.scalar()

        if not delete_account:
            raise EntityDoesNotExist(f"Service with id `{id}` does not exist!")  # type: ignore

        stmt = sqlalchemy.delete(table=Service).where(Service.id == delete_account.id)

        await self.async_session.execute(statement=stmt)
        await self.async_session.commit()

        return f"Service with id '{id}' is successfully deleted!"
