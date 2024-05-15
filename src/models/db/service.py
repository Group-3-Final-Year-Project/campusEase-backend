import datetime
import sqlalchemy
from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column as sqlalchemy_mapped_column
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.repository.table import Base

class Service(Base):
    __tablename__ = 'service'
    
    id:SQLAlchemyMapped[str] = sqlalchemy_mapped_column(primary_key=True)
    name: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(
        sqlalchemy.String(length=64), nullable=False, unique=True
    )
    # other attributes that we will need for service will be added here