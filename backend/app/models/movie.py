from sqlalchemy import String, Text, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    language: Mapped[str | None] = mapped_column(String(50), nullable=True)
    genre: Mapped[str | None] = mapped_column(String(100), nullable=True)
    release_date: Mapped[Date | None] = mapped_column(Date, nullable=True)
    rating: Mapped[str | None] = mapped_column(String(10), nullable=True)

    shows: Mapped[list["Show"]] = relationship(back_populates="movie")