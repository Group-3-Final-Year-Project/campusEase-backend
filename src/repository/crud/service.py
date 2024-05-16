import typing
import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.service import Service
from src.models.schemas.service import ServiceInCreate,ServiceInUpdate
from src.repository.crud.base import BaseCRUDRepository

class ServiceCRUDRepository(BaseCRUDRepository):
    async def create_service(self,service_create:ServiceInCreate) -> Service:
        # new_service = Service()
        pass

    async def read_services(self) -> typing.Sequence[Service]:
        pass

    async def read_service_by_id(self,id:str) -> Service:
        pass

    async def read_services_by_name(self,name:str) -> typing.Sequence[Service]:
        pass

    async def update_service_by_id(self,id:str,service_update:ServiceInUpdate) -> Service:
        pass

    async def delete_service_by_id(self,id:str) -> str:
        pass