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
        service =  ServiceInResponse(
        id=db_service.id,
        provider_id=db_service.provider_id,
        name=db_service.name,
        description=db_service.description,
        category=db_service.category,
        location=db_service.location,
        cover_image=db_service.cover_image,
        gallery=db_service.gallery,
        email=db_service.email,
        website=db_service.website,
        starting_prices=db_service.starting_prices,
        created_at=db_service.created_at,
        updated_at=db_service.updated_at,
        is_available=db_service.is_available
    )
        db_service_list.append(service)
    
    return db_service_list

@router.get(
    path="/categories",
    name="services:get_categories",
    status_code=fastapi.status.HTTP_200_OK
)
async def get_service_categories(service_repo:ServiceCRUDRepository = fastapi.Depends(get_repository(repo_type=ServiceCRUDRepository))):
    pass

@router.get(
    path="/categories/{id}",
    response_model=list[ServiceInResponse],
    name="services:get_services_by_category",
    status_code=fastapi.status.HTTP_200_OK
)
async def get_services_by_category(category_id:int,service_repo:ServiceCRUDRepository = fastapi.Depends(get_repository(repo_type=ServiceCRUDRepository))) -> list[ServiceInResponse]:
    pass


@router.get(
    path="/near/{latitude}&{longitude}",
    response_model=list[ServiceInResponse],
    name="services:get_services_near_a_location",
    status_code=fastapi.status.HTTP_200_OK
)
async def get_services_near_a_location(latitide:float,longitude:float,service_repo:ServiceCRUDRepository = fastapi.Depends(get_repository(repo_type=ServiceCRUDRepository))) -> list[ServiceInResponse]:
    pass

@router.get(
    path="/{id}",
    name="services:read-service-by-id",
    response_model=ServiceInResponse,
    status_code=fastapi.status.HTTP_200_OK
)
async def get_service(
    id:int,
    service_repo:ServiceCRUDRepository = fastapi.Depends(get_repository(repo_type=ServiceCRUDRepository))
) -> ServiceInResponse:
    try:
        db_service = await service_repo.read_service_by_id(id=id)
    except EntityDoesNotExist:
        raise await http_404_exc_id_not_found_request(id=id)
    
    return ServiceInResponse(
        id=db_service.id,
        provider_id=db_service.provider_id,
        name=db_service.name,
        description=db_service.description,
        category=db_service.category,
        location=db_service.location,
        cover_image=db_service.cover_image,
        gallery=db_service.gallery,
        email=db_service.email,
        website=db_service.website,
        starting_prices=db_service.starting_prices,
        created_at=db_service.created_at,
        updated_at=db_service.updated_at,
        is_available=db_service.is_available
    )


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
    new_service = await service_repo.create_service(service_create=service_create)
    return ServiceInResponse(
        id=new_service.id,
        provider_id=new_service.provider_id,
        name=new_service.name,
        description=new_service.description,
        category=new_service.category,
        location=new_service.location,
        cover_image=new_service.cover_image,
        gallery=new_service.gallery,
        email=new_service.email,
        website=new_service.website,
        starting_prices=new_service.starting_prices,
        created_at=new_service.created_at,
        updated_at=new_service.updated_at,
        is_available=new_service.is_available
    )

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
    
    return ServiceInResponse(
        id=updated_db_service.id,
        provider_id=updated_db_service.provider_id,
        name=updated_db_service.name,
        description=updated_db_service.description,
        category=updated_db_service.category,
        location=updated_db_service.location,
        cover_image=updated_db_service.cover_image,
        gallery=updated_db_service.gallery,
        email=updated_db_service.email,
        website=updated_db_service.website,
        starting_prices=updated_db_service.starting_prices,
        created_at=updated_db_service.created_at,
        updated_at=updated_db_service.updated_at,
        is_available=updated_db_service.is_available
    )

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

