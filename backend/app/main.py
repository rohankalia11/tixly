from fastapi import FastAPI
from sqlalchemy import text

from app.database.session import engine
from app.api.movies import router as movies_router

app = FastAPI(title="Movie Ticket Booking Platform")

app.include_router(movies_router)


@app.get("/health")
def health_check():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"

    return {"status": "healthy", "database": db_status}