from sqlalchemy import Integer, ForeignKey, String, Numeric, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from decimal import Decimal

from app.models.base import Base


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)
    show_id: Mapped[int] = mapped_column(ForeignKey("shows.id", ondelete="RESTRICT"), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    user: Mapped["User"] = relationship(back_populates="bookings")
    booking_seats: Mapped[list["BookingSeat"]] = relationship(back_populates="booking", cascade="all, delete-orphan")
    payment: Mapped["Payment | None"] = relationship(back_populates="booking", cascade="all, delete-orphan")