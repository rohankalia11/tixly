from sqlalchemy import Integer, ForeignKey, DateTime, Numeric, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from decimal import Decimal

from app.models.base import Base


class Show(Base):
    __tablename__ = "shows"
    __table_args__ = (
        UniqueConstraint("screen_id", "start_time", name="uq_screen_start_time"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id", ondelete="CASCADE"), nullable=False)
    screen_id: Mapped[int] = mapped_column(ForeignKey("screens.id", ondelete="CASCADE"), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    base_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    movie: Mapped["Movie"] = relationship(back_populates="shows")
    screen: Mapped["Screen"] = relationship(back_populates="shows")
    show_seats: Mapped[list["ShowSeat"]] = relationship(back_populates="show", cascade="all, delete-orphan")