import fastapi

router = fastapi.APIRouter(prefix="/bookings",tags=['bookings'])

@router.get()
async def get_bookings():
    pass

@router.get()
async def get_booking():
    pass

@router.post()
async def create_booking():
    pass

@router.patch()
async def update_booking():
    pass

@router.delete()
async def delete_booking():
    pass

