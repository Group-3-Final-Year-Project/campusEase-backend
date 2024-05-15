import fastapi
import pydantic

router = fastapi.APIRouter(prefix='/services',tags=['services'])

@router.get()
async def get_services():
    pass

@router.get()
async def get_service():
    pass

@router.post()
async def create_service():
    pass

@router.patch()
async def update_service():
    pass

@router.delete()
async def delete_service():
    pass
