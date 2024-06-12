import datetime
import json
import sqlalchemy
from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column as sqlalchemy_mapped_column
from sqlalchemy.sql import functions as sqlalchemy_functions
from sqlalchemy.orm import relationship

from src.repository.table import Base

class Service(Base):
    __tablename__ = 'service'
    
    id:SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True,autoincrement=True)
    provider_id:SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("account.id"),nullable=False)
    name: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(
        sqlalchemy.String(length=100), nullable=False
    )
    description: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.Text(), nullable=True)
    category: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(length=100), nullable=False)
    cover_image: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(),nullable=True)
    gallery: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.JSON)
    starting_prices: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.JSON)
    email: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(),nullable=True)
    website: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(),nullable=True)
    location: SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(),nullable=True)
    is_available: SQLAlchemyMapped[bool] = sqlalchemy_mapped_column(sqlalchemy.Boolean, nullable=False, default=True)
    created_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=False, server_default=sqlalchemy_functions.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=True,
        server_onupdate=sqlalchemy.schema.FetchedValue(for_update=True),
    )
    # other attributes that we will need for service will be added here

    account = relationship("Account", backref="service")
    __mapper_args__ = {"eager_defaults": True}