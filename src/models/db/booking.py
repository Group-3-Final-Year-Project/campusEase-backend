import datetime
import sqlalchemy
from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column as sqlalchemy_mapped_column,relationship
from sqlalchemy.sql import functions as sqlalchemy_functions

from src.repository.table import Base

class Booking(Base):
    __tablename__ = 'booking'
    
    id:SQLAlchemyMapped[int] = sqlalchemy_mapped_column(primary_key=True,autoincrement=True)
    service_id:SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("service.id"),nullable=False)
    provider_id:SQLAlchemyMapped[int] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("account.id"),nullable=False)
    user_id:SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.ForeignKey("account.id",),nullable=False)
    scheduled_service_date:SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=True, server_default=sqlalchemy_functions.now())
    service_cost:SQLAlchemyMapped[float] = sqlalchemy_mapped_column(sqlalchemy.Float(),nullable=False)
    payment_method:SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(),nullable=False)
    service_address:SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(),nullable=True)
    booking_details:SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(),nullable=True)
    booking_attachments:SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(),nullable=True)
    booking_status:SQLAlchemyMapped[str] = sqlalchemy_mapped_column(sqlalchemy.String(),nullable=False)
    booking_date:SQLAlchemyMapped[datetime.datetime] = sqlalchemy_mapped_column(
    sqlalchemy.DateTime(timezone=True), nullable=False, server_default=sqlalchemy_functions.now()
    )
    # other attributes that we will need for booking will be added here
    user_account = relationship("Account", foreign_keys="Booking.user_id", backref="booking_with_user_id")
    provider_account = relationship("Account", foreign_keys="Booking.provider_id", backref="booking_with_provider_id")
    service = relationship("Service", backref="booking")
    __mapper_args__ = {"eager_defaults": True}
