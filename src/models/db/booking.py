import datetime
import sqlalchemy
from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column as sqlalchemy_mapped_column,relationship
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.repository.table import Base

class Booking(Base):
    __tablename__ = 'booking'
    
    id:SQLAlchemyMapped[str] = sqlalchemy_mapped_column(primary_key=True)
    service_id:SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("service.id"),nullable=False)
    provider_id:SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("account.id"),nullable=False)
    
    # other attributes that we will need for booking will be added here
    # provider = relationship("Account", backref="services")
    __mapper_args__ = {"eager_defaults": True}
