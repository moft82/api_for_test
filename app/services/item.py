import os
from fastapi import HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.crud.item import create_item_db, delete_item_db, read_all_items_db, read_item_by_id_and_user_db, read_items_by_user_id_db, update_item_db
from app.db.models.item import Item
from app.error.item import DeleteError, InvalidFilePathError, ItemNotFoundError, UpdateError
from app.schemas.item import ItemUpdate, ItemCreate
from app.utils.file_util import save_file

# GET
def read_all_items_sv(db: Session) -> Item:
    item = read_all_items_db(db)
    if not item:
        raise ItemNotFoundError()
    return item

# Get all items belonging to a user by user_id
def read_items_by_user_id_sv(db: Session, user_id: int):
    items = read_items_by_user_id_db(db, user_id)
    if not items:
        raise ItemNotFoundError(user_id=user_id)
    return items

# Get all items belonging to a user by user_id
def read_item_by_id_and_user_id_sv(db: Session, item_id:int, user_id: int):
    items = read_item_by_id_and_user_db(db, item_id, user_id)
    if not items:
        raise ItemNotFoundError(item_id=item_id, user_id=user_id)
    return items

# Function to handle the business logic of downloading a file
def download_item_file(db: Session, item_id: int, user_id: int):
    # Fetch item details from the database
    item = read_item_by_id_and_user_db(db, item_id, user_id)
    
    # Get the file path from the item
    file_path = item.file_path

    # Check if the file exists on the server
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    # Serve the file
    return FileResponse(path=file_path, filename=os.path.basename(file_path), media_type="application/octet-stream")


# POST
def create_item_sv(db: Session, item_data: dict, file:UploadFile, user_id:int) -> Item:
    # Set Save Path
    upload_dir = f"uploads/{user_id}"
    
    # Save the file and get the path
    try:
        file_path = save_file(file, upload_dir)
    except Exception as e:
        raise InvalidFilePathError(upload_dir)  # Handle any issues with file saving
    
    item_data["user_id"] = user_id
    item_data["file_path"] = file_path
    
    new_item = ItemCreate(**item_data)
    return create_item_db(db=db, item_data=new_item)

# PUT
def update_item_sv(db: Session, item_id: int, user_id:int, item_data: ItemUpdate) -> Item:
    item = read_item_by_id_and_user_db(db, item_id, user_id)
    if not item:
        raise ItemNotFoundError(item_id=item_id, user_id=user_id)
    
    updated_item = update_item_db(db=db, item=item, item_data=item_data)
    if not updated_item:
        raise UpdateError(item_id=item_id)
    return updated_item

# DELETE
def delete_item_sv(db: Session, item_id: int, user_id:int):
    if not delete_item_db(db, item_id, user_id):
        raise DeleteError(item_id=item_id)

