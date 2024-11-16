from datetime import datetime
import os
from fastapi import UploadFile
from uuid import uuid4

def save_file(file: UploadFile, UPLOAD_DIR:str) -> str:
    # Ensure the uploads directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    
    # Create a unique filename with UUID and timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid4()}_{timestamp}{file_extension}"
    file_location = os.path.join(UPLOAD_DIR, unique_filename)

    # Save the file to the specified location
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    
    return file_location
