import fastapi
import pydantic

from src.api.dependencies.repository import get_repository
from src.repository.crud.service import ServiceCRUDRepository
from src.models.schemas.service import ServiceInResponse,ServiceInUpdate,ServiceInCreate
from src.utilities.exceptions.database import EntityDoesNotExist
from src.utilities.exceptions.http.exc_404 import (
    http_404_exc_email_not_found_request,
    http_404_exc_id_not_found_request,
    http_404_exc_username_not_found_request,
)



router = fastapi.APIRouter(prefix='/services',tags=['services'])

@router.get(
    path="",
    name="services:read-services",
    response_model=list[ServiceInResponse],
    status_code=fastapi.status.HTTP_200_OK
)
async def get_services(
    service_repo:ServiceCRUDRepository = fastapi.Depends(get_repository(repo_type=ServiceCRUDRepository))
) -> list[ServiceInResponse]:
    db_services = await service_repo.read_services()
    db_service_list:list = list()

    for db_service in db_services:
        service = ServiceInResponse(**db_service)
        db_service_list.append(service)
    
    return db_service_list

@router.get(
    path="/{id}",
    name="services:read-service-by-id",
    response_model=ServiceInResponse,
    status_code=fastapi.status.HTTP_200_OK
)
async def get_service(
    id:str,
    service_repo:ServiceCRUDRepository = fastapi.Depends(get_repository(repo_type=ServiceCRUDRepository))
) -> ServiceInResponse:
    try:
        db_service = await service_repo.read_service_by_id(id=id)
    except EntityDoesNotExist:
        raise await http_404_exc_id_not_found_request(id=id)
    
    return ServiceInResponse(**db_service)


@router.post(
    path="",
    name="services:create-service",
    response_model=ServiceInResponse,
    status_code=fastapi.status.HTTP_201_CREATED
)
async def create_service(
    service_create:ServiceInCreate,
      service_repo:ServiceCRUDRepository = fastapi.Depends(get_repository(repo_type=ServiceCRUDRepository))
) -> ServiceInResponse:
    new_service = await service_repo.create_service(service_create=service)
    return ServiceInResponse(**new_service)

@router.patch(
    path="/{id}",
    name="services:update-service-by-id",
    response_model=ServiceInResponse,
    status_code=fastapi.status.HTTP_200_OK
)
async def update_service(
    query_id:str,
    #include other arguments here
    service_repo:ServiceCRUDRepository = fastapi.Depends(get_repository(repo_type=ServiceCRUDRepository))
) -> ServiceInResponse:
    service_update = ServiceInUpdate()
    try:
        updated_db_service = await service_repo.update_service_by_id(id=query_id,service_update=service_update)
    except EntityDoesNotExist:
        raise await http_404_exc_id_not_found_request(id=query_id)
    
    return ServiceInResponse(**updated_db_service)

@router.delete(
    path="",
    name="services:delete-service-by-id",
    status_code=fastapi.status.HTTP_200_OK
)
async def delete_service(
    id:str,
    service_repo:ServiceCRUDRepository = fastapi.Depends(get_repository(repo_type=ServiceCRUDRepository))
) -> dict[str,str]:
    try:
        deletion_result = await service_repo.delete_service_by_id(id=id)
    except EntityDoesNotExist:
        raise await http_404_exc_id_not_found_request(id=id)
    return {"notification":deletion_result}
