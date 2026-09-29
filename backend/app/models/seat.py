from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Seat(Base):
    __tablename__ = "seats"
    __table_args__ = (
        UniqueConstraint("screen_id", "row_label", "seat_number", name="uq_seat_position"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    screen_id: Mapped[int] = mapped_column(ForeignKey("screens.id", ondelete="CASCADE"), nullable=False)
    row_label: Mapped[str] = mapped_column(String(5), nullable=False)
    seat_number: Mapped[int] = mapped_column(Integer, nullable=False)
    seat_type: Mapped[str] = mapped_column(String(20), nullable=False, default="regular")

    screen: Mapped["Screen"] = relationship(back_populates="seats")
    show_seats: Mapped[list["ShowSeat"]] = relationship(back_populates="seat")