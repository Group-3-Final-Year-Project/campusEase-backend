import typing
import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.models.db.review import Review
from src.models.schemas.review import ReviewInCreate,ReviewInUpdate
from src.repository.crud.base import BaseCRUDRepository
from src.utilities.exceptions.database import EntityAlreadyExists, EntityDoesNotExist

class ReviewCRUDRepository(BaseCRUDRepository):
    async def create_review(self,review_create:ReviewInCreate) -> Review:
        new_review = Review(**review_create)
        self.async_session.add(instance=new_review)
        await self.async_session.commit()
        await self.async_session.refresh(instance=new_review)
        

    async def read_reviews(self) -> typing.Sequence[Review]:
        stmt = sqlalchemy.select(Review)
        query = await self.async_session.execute(statement=stmt)
        return query.scalars().all()

    async def read_review_by_id(self,id:str) -> Review:
        stmt = sqlalchemy.select(Review).where(Review.id == id)
        query = await self.async_session.execute(statement=stmt)

        if not query:
            raise EntityDoesNotExist(f"Review with id `{id}` does not exist!")
        return query.scalar()

    async def read_reviews_by_name(self,name:str) -> typing.Sequence[Review]:
        stmt = sqlalchemy.select(Review).where(name in Review.name)
        query = await self.async_session.execute(statement=stmt)

        if not query:
            raise EntityDoesNotExist("Reviews with name `{name}` does not exist!".format(name=name)) 
        
        return query.scalars().all()

    async def update_review_by_id(self,id:str,review_update:ReviewInUpdate) -> Review:
        new_review_data = review_update.dict()
        select_stmt = sqlalchemy.select(Review).where(Review.id == id)
        query = await self.async_session.execute(statement=select_stmt)
        update_review = query.scalar()

        if not update_account:
            raise EntityDoesNotExist(f"Review with id `{id}` does not exist!")

        update_stmt = sqlalchemy.update(table=Review).where(Review.id == update_review.id).values(updated_at=sqlalchemy_functions.now(),**new_review_data)

        await self.async_session.execute(statement=update_stmt)
        await self.async_session.commit()
        await self.async_session.refresh(instance=update_review)

        return update_review


    async def delete_review_by_id(self,id:str) -> str:
        select_stmt = sqlalchemy.select(Review).where(Review.id == id)
        query = await self.async_session.execute(statement=select_stmt)
        delete_account = query.scalar()

        if not delete_account:
            raise EntityDoesNotExist(f"Review with id `{id}` does not exist!")  # type: ignore

        stmt = sqlalchemy.delete(table=Review).where(Review.id == delete_account.id)

        await self.async_session.execute(statement=stmt)
        await self.async_session.commit()

        return f"Review with id '{id}' is successfully deleted!"
