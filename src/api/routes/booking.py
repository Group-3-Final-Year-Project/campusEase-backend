import fastapi
import pydantic

from src.api.dependencies.repository import get_repository
from src.repository.crud.booking import BookingCRUDRepository
from src.models.schemas.booking import BookingInResponse,BookingInUpdate,BookingInCreate
from src.utilities.exceptions.database import EntityDoesNotExist
from src.utilities.exceptions.http.exc_404 import (
    http_404_exc_email_not_found_request,
    http_404_exc_id_not_found_request,
    http_404_exc_username_not_found_request,
)


router = fastapi.APIRouter(prefix="/bookings",tags=['bookings'])

@router.get(
    path="",
    name="bookings:read_bookings",
    response_model=list[BookingInResponse],
    status_code=fastapi.status.HTTP_200_OK
)
async def get_bookings(
    booking_repo:BookingCRUDRepository = fastapi.Depends(get_repository(repo_type=BookingCRUDRepository))
) -> list[BookingInResponse]:
    db_bookings = await booking_repo.read_bookings()
    db_booking_list:list = list()

    for db_booking in db_bookings:
        booking = BookingInResponse(**db_booking)
        db_booking_list.append(booking)
    
    return db_booking_list


@router.get(path="/{id}",
    name="bookings:read-booking-by-id",
    response_model=BookingInResponse,
    status_code=fastapi.status.HTTP_200_OK)
async def get_booking(id:str,booking_repo:BookingCRUDRepository = fastapi.Depends(get_repository(repo_type=BookingCRUDRepository)))-> BookingInResponse:
    try:
        db_booking = await booking_repo.read_booking_by_id(id=id)
    except EntityDoesNotExist:
        raise await http_404_exc_id_not_found_request(id=id)
    
    return BookingInResponse(**db_booking)


@router.post(
    path="",
    name="bookings:create-booking",
    response_model=BookingInResponse,
    status_code=fastapi.status.HTTP_201_CREATED
)
async def create_booking(
    booking_create:BookingInCreate,
      booking_repo:BookingCRUDRepository = fastapi.Depends(get_repository(repo_type=BookingCRUDRepository))
) -> BookingInResponse:
    new_booking = await booking_repo.create_booking(booking_create=booking)
    return BookingInResponse(**new_booking)

@router.patch(
    path="/{id}",
    name="bookings:update-booking-by-id",
    response_model=BookingInResponse,
    status_code=fastapi.status.HTTP_200_OK
)
async def update_booking(
    query_id:str,
    #include other arguments here
    booking_repo:BookingCRUDRepository = fastapi.Depends(get_repository(repo_type=BookingCRUDRepository))
) -> BookingInResponse:
    booking_update = BookingInUpdate()
    try:
        updated_db_booking = await booking_repo.update_booking_by_id(id=query_id,booking_update=booking_update)
    except EntityDoesNotExist:
        raise await http_404_exc_id_not_found_request(id=query_id)
    
    return BookingInResponse(**updated_db_booking)

@router.delete(
    path="",
    name="bookings:delete-booking-by-id",
    status_code=fastapi.status.HTTP_200_OK
)
async def delete_booking(
    id:str,
    booking_repo:BookingCRUDRepository = fastapi.Depends(get_repository(repo_type=BookingCRUDRepository))
) -> dict[str,str]:
    try:
        deletion_result = await booking_repo.delete_booking_by_id(id=id)
    except EntityDoesNotExist:
        raise await http_404_exc_id_not_found_request(id=id)
    return {"notification":deletion_result}
