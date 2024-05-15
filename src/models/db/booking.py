import datetime
import sqlalchemy
from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column as sqlalchemy_mapped_column
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.repository.table import Base

class Booking(Base):
    __tablename__ = 'booking'
    
    id:SQLAlchemyMapped[str] = sqlalchemy_mapped_column(primary_key=True)
    # other attributes that we will need for booking will be added here