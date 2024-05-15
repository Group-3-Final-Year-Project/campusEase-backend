import fastapi
import pydantic

router = fastapi.APIRouter(prefix='/reviews',tags=['reviews'])

@router.get()
async def get_reviews():
    pass

@router.get()
async def get_review():
    pass

@router.post()
async def create_review():
    pass

@router.patch()
async def update_review():
    pass

@router.delete()
async def delete_review():
    pass
