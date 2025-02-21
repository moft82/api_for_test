from starlette.middleware.base import BaseHTTPMiddleware
import time
from app.core.logging_config import logger
from sqlalchemy.exc import SQLAlchemyError

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        
        # Log incoming request details
        logger.info(f"Incoming request: {request.method} {request.url}")
        logger.info(f"Headers: {dict(request.headers)}")
        logger.info(f"Query Params: {dict(request.query_params)}")

        try:
            # Process the request and get response
            response = await call_next(request)

            # Log response status and process time
            process_time = time.time() - start_time
            logger.info(f"Response status: {response.status_code} in {process_time:.4f}s")
            
        except SQLAlchemyError as exc:
            process_time = time.time() - start_time
            logger.error(
                f"SQLAlchemyError during request: {request.method} {request.url} "
                f"after {process_time:.4f}s - {str(exc)}",
                exc_info=True
            )
            raise exc  # Pass the error to the centralized handler
        except Exception as exc:
            process_time = time.time() - start_time
            logger.error(
                f"Exception during request: {request.method} {request.url} "
                f"after {process_time:.4f}s - {str(exc)}",
                exc_info=True
            )
            raise exc

        return response
