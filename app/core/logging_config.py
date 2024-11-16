# logging_config.py
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app_logs.txt"),  # Save to file
        logging.StreamHandler()  # Also log to console (optional)
    ]
)

logger = logging.getLogger("app_logger")
