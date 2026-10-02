from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.repositories.movie_repository import MovieRepository
from app.services.movie_service import MovieService


def get_movie_service(db: Session = Depends(get_db)) -> MovieService:
    repository = MovieRepository(db)
    return MovieService(repository)