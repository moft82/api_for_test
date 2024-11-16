from fastapi import FastAPI
from app.core.config import Config
from app.api.routers import auth, item, status, websocket, manage
from app.db.database import Base, db
from fastapi.staticfiles import StaticFiles
import uvicorn
from app.middleware.logging import LoggingMiddleware

def create_app() -> FastAPI:
    config = Config()  
    app = FastAPI(debug=config.DEBUG)
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    # Apply logging middleware
    app.add_middleware(LoggingMiddleware)

    app.include_router(auth.router)
    app.include_router(item.router)
    app.include_router(websocket.router)
    
    app.include_router(status.router)
    app.include_router(manage.router)

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