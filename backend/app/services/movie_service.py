from fastapi import HTTPException, status

from app.repositories.movie_repository import MovieRepository
from app.schemas.movie import MovieCreate, MovieUpdate
from app.models.movie import Movie


class MovieService:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def get_movie(self, movie_id: int) -> Movie:
        movie = self.repository.get_by_id(movie_id)
        if not movie:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
        return movie

    def list_movies(self, skip: int = 0, limit: int = 20) -> list[Movie]:
        return self.repository.get_all(skip=skip, limit=limit)

    def create_movie(self, movie_data: MovieCreate) -> Movie:
        if movie_data.duration_minutes <= 0:
            raise HTTPException(status_code=400, detail="Duration must be positive")
        return self.repository.create(movie_data)

    def update_movie(self, movie_id: int, movie_data: MovieUpdate) -> Movie:
        movie = self.get_movie(movie_id)
        return self.repository.update(movie, movie_data)

    def delete_movie(self, movie_id: int) -> None:
        movie = self.get_movie(movie_id)
        self.repository.delete(movie)