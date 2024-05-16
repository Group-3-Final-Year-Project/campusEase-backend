import fastapi
import pydantic

router = fastapi.APIRouter(prefix='/reviews',tags=['reviews'])

@router.get(path="")
async def get_reviews():
    pass

@router.get(path="/{id}")
async def get_review():
    pass

@router.post(path="")
async def create_review():
    pass

@router.patch(path="/{id}")
async def update_review():
    pass

@router.delete(path="")
async def delete_review():
    pass
