from fastapi import FastAPI
import uvicorn
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import config
from app.api.routers import auth, item, websocket
from app.middlewares.logging import LoggingMiddleware
from app.errors.handler import sqlalchemy_exception_handler
from app.db.database import Base, db

def create_app() -> FastAPI:
    app = FastAPI(debug=config.DEBUG)    
    # Apply logging middleware
    app.add_middleware(LoggingMiddleware)
    
    # Register SQLAlchemyError handler
    app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)

    app.include_router(auth.router)
    app.include_router(item.router)
    app.include_router(websocket.router)

    return app

app = create_app()

# Create tables
Base.metadata.create_all(bind=db.engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    # uvicorn.run("app.main:app", host="127.0.0.1", port=8000)
    uvicorn.run("app", host="127.0.0.1", port=8000)

# uvicorn app.main:app --reload