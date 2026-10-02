from pydantic import BaseModel
from datetime import date


class MovieBase(BaseModel):
    title: str
    description: str | None = None
    duration_minutes: int
    language: str | None = None
    genre: str | None = None
    release_date: date | None = None
    rating: str | None = None


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    duration_minutes: int | None = None
    language: str | None = None
    genre: str | None = None
    release_date: date | None = None
    rating: str | None = None


class MovieResponse(MovieBase):
    id: int

    class Config:
        from_attributes = True