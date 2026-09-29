from sqlalchemy import Integer, ForeignKey, String, Numeric, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal

from app.models.base import Base


class ShowSeat(Base):
    __tablename__ = "show_seats"
    __table_args__ = (
        UniqueConstraint("show_id", "seat_id", name="uq_show_seat"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    show_id: Mapped[int] = mapped_column(ForeignKey("shows.id", ondelete="CASCADE"), nullable=False)
    seat_id: Mapped[int] = mapped_column(ForeignKey("seats.id", ondelete="CASCADE"), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="available")
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    show: Mapped["Show"] = relationship(back_populates="show_seats")
    seat: Mapped["Seat"] = relationship(back_populates="show_seats")
    booking_seat: Mapped["BookingSeat | None"] = relationship(back_populates="show_seat")