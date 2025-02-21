from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    """
    Global handler for SQLAlchemy errors.
    Captures the error message and returns a client-safe response.
    """
    error_message = str(exc.__dict__.get("orig", exc))  # Extract the SQLAlchemy error message
    return JSONResponse(
        status_code=500,
        content={"detail": f"Database error: {error_message}"},
    )