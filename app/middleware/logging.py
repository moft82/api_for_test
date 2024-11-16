from starlette.middleware.base import BaseHTTPMiddleware
import time
from app.middleware.logging import logger

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        
        # Log the request
        logger.info(f"Incoming request: {request.method} {request.url}")
        
        # Process the request and get response
        response = await call_next(request)
        
        # Log the response status and process time
        process_time = time.time() - start_time
        logger.info(f"Response status: {response.status_code} in {process_time:.4f}s")
        
        return response
