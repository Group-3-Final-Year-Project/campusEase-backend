import fastapi

router = fastapi.APIRouter(prefix="/bookings",tags=['bookings'])

@router.get(path="")
async def get_bookings():
    pass

@router.get(path="/{id}")
async def get_booking():
    pass

@router.post(path="")
async def create_booking():
    pass

@router.patch(path="/{id}")
async def update_booking():
    pass

@router.delete(path="")
async def delete_booking():
    pass
