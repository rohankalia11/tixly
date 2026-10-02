from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieUpdate


class MovieRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, movie_id: int) -> Movie | None:
        return self.db.get(Movie, movie_id)

    def get_all(self, skip: int = 0, limit: int = 20) -> list[Movie]:
        stmt = select(Movie).offset(skip).limit(limit)
        return list(self.db.execute(stmt).scalars().all())

    def create(self, movie_data: MovieCreate) -> Movie:
        movie = Movie(**movie_data.model_dump())
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie

    def update(self, movie: Movie, movie_data: MovieUpdate) -> Movie:
        update_data = movie_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(movie, field, value)
        self.db.commit()
        self.db.refresh(movie)
        return movie

    def delete(self, movie: Movie) -> None:
        self.db.delete(movie)
        self.db.commit()