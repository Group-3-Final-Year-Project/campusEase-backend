import fastapi
import pydantic

from src.api.dependencies.repository import get_repository
from src.repository.crud.review import ReviewCRUDRepository
from src.models.schemas.review import ReviewInResponse,ReviewInUpdate,ReviewInCreate
from src.utilities.exceptions.database import EntityDoesNotExist
from src.utilities.exceptions.http.exc_404 import (
    http_404_exc_email_not_found_request,
    http_404_exc_id_not_found_request,
    http_404_exc_username_not_found_request,
)



router = fastapi.APIRouter(prefix='/reviews',tags=['reviews'])

@router.get(
    path="",
    name="reviews:read-reviews",
    response_model=list[ReviewInResponse],
    status_code=fastapi.status.HTTP_200_OK
)
async def get_reviews(
    review_repo:ReviewCRUDRepository = fastapi.Depends(get_repository(repo_type=ReviewCRUDRepository))
) -> list[ReviewInResponse]:
    db_reviews = await review_repo.read_reviews()
    db_review_list:list = list()

    for db_review in db_reviews:
        review = ReviewInResponse(**db_review)
        db_review_list.append(review)
    
    return db_review_list

@router.get(
    path="/{id}",
    name="reviews:read-review-by-id",
    response_model=ReviewInResponse,
    status_code=fastapi.status.HTTP_200_OK
)
async def get_review(
    id:str,
    review_repo:ReviewCRUDRepository = fastapi.Depends(get_repository(repo_type=ReviewCRUDRepository))
) -> ReviewInResponse:
    try:
        db_review = await review_repo.read_review_by_id(id=id)
    except EntityDoesNotExist:
        raise await http_404_exc_id_not_found_request(id=id)
    
    return ReviewInResponse(**db_review)


@router.post(
    path="",
    name="reviews:create-review",
    response_model=ReviewInResponse,
    status_code=fastapi.status.HTTP_201_CREATED
)
async def create_review(
    review_create:ReviewInCreate,
      review_repo:ReviewCRUDRepository = fastapi.Depends(get_repository(repo_type=ReviewCRUDRepository))
) -> ReviewInResponse:
    new_review = await review_repo.create_review(review_create=review)
    return ReviewInResponse(**new_review)

@router.patch(
    path="/{id}",
    name="reviews:update-review-by-id",
    response_model=ReviewInResponse,
    status_code=fastapi.status.HTTP_200_OK
)
async def update_review(
    query_id:str,
    #include other arguments here
    review_repo:ReviewCRUDRepository = fastapi.Depends(get_repository(repo_type=ReviewCRUDRepository))
) -> ReviewInResponse:
    review_update = ReviewInUpdate()
    try:
        updated_db_review = await review_repo.update_review_by_id(id=query_id,review_update=review_update)
    except EntityDoesNotExist:
        raise await http_404_exc_id_not_found_request(id=query_id)
    
    return ReviewInResponse(**updated_db_review)

@router.delete(
    path="",
    name="reviews:delete-review-by-id",
    status_code=fastapi.status.HTTP_200_OK
)
async def delete_review(
    id:str,
    review_repo:ReviewCRUDRepository = fastapi.Depends(get_repository(repo_type=ReviewCRUDRepository))
) -> dict[str,str]:
    try:
        deletion_result = await review_repo.delete_review_by_id(id=id)
    except EntityDoesNotExist:
        raise await http_404_exc_id_not_found_request(id=id)
    return {"notification":deletion_result}
