import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app_logs.txt", encoding="utf-8"),  # Log to file with UTF-8 encoding
        logging.StreamHandler(),  # Log to console
    ]
)

# Create a named logger for the application
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# Example: Add specific format for a handler (Optional)
file_handler = logging.FileHandler("app_logs.txt", encoding="utf-8")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)
