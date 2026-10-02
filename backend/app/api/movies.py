from fastapi import APIRouter, Depends

from app.services.movie_service import MovieService
from app.schemas.movie import MovieCreate, MovieUpdate, MovieResponse
from app.api.deps import get_movie_service

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, service: MovieService = Depends(get_movie_service)):
    return service.get_movie(movie_id)


@router.get("/", response_model=list[MovieResponse])
def list_movies(skip: int = 0, limit: int = 20, service: MovieService = Depends(get_movie_service)):
    return service.list_movies(skip=skip, limit=limit)


@router.post("/", response_model=MovieResponse, status_code=201)
def create_movie(movie_data: MovieCreate, service: MovieService = Depends(get_movie_service)):
    return service.create_movie(movie_data)


@router.patch("/{movie_id}", response_model=MovieResponse)
def update_movie(movie_id: int, movie_data: MovieUpdate, service: MovieService = Depends(get_movie_service)):
    return service.update_movie(movie_id, movie_data)


@router.delete("/{movie_id}", status_code=204)
def delete_movie(movie_id: int, service: MovieService = Depends(get_movie_service)):
    service.delete_movie(movie_id)