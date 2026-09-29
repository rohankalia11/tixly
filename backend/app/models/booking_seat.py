from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class BookingSeat(Base):
    __tablename__ = "booking_seats"

    id: Mapped[int] = mapped_column(primary_key=True)
    booking_id: Mapped[int] = mapped_column(ForeignKey("bookings.id", ondelete="CASCADE"), nullable=False)
    show_seat_id: Mapped[int] = mapped_column(ForeignKey("show_seats.id", ondelete="RESTRICT"), unique=True, nullable=False)

    booking: Mapped["Booking"] = relationship(back_populates="booking_seats")
    show_seat: Mapped["ShowSeat"] = relationship(back_populates="booking_seat")