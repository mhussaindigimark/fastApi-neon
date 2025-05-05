from fastapi import FastAPI
from app.routes.base import router as base_router
from app.database.connection import Base, engine

def create_app():
    app = FastAPI(
        title="FastAPI Neon Boilerplate",
        description="Boilerplate for FastAPI with Neon DB",
        version="0.1.0"
    )
    
    # Create database tables
    Base.metadata.create_all(bind=engine)
    
    # Include routers
    app.include_router(base_router, prefix="/api/v1")
    
    return app

app = create_app()