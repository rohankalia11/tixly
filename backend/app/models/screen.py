from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Screen(Base):
    __tablename__ = "screens"

    id: Mapped[int] = mapped_column(primary_key=True)
    theatre_id: Mapped[int] = mapped_column(ForeignKey("theatres.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    total_seats: Mapped[int] = mapped_column(Integer, nullable=False)

    theatre: Mapped["Theatre"] = relationship(back_populates="screens")
    seats: Mapped[list["Seat"]] = relationship(back_populates="screen", cascade="all, delete-orphan")
    shows: Mapped[list["Show"]] = relationship(back_populates="screen")