from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.database import get_db
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse
from app.services.item import (
    create_new_item_sv,
    delete_item_sv,
    get_item_by_id_sv,
    get_items_sv,
    update_item_by_id_sv,
)
from app.errors.item import ItemNotFoundError, UpdateError, DeleteError

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not Found"}},
)

# Get all items
@router.get("/", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    """
    Retrieve all items.
    """
    try:
        items = get_items_sv(db)
        return items
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Get an item by ID
@router.get("/{item_id}", response_model=ItemResponse)
def get_item_by_id(item_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single item by its ID.
    """
    try:
        item = get_item_by_id_sv(db, item_id)
        return item
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Create a new item
@router.post("/", response_model=ItemResponse)
def create_item(item_data: ItemCreate, db: Session = Depends(get_db)):
    """
    Create a new item.
    """
    try:
        return create_new_item_sv(db, item_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error occurred while creating the item.")


# Update an item by ID
@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item_data: ItemUpdate, db: Session = Depends(get_db)):
    """
    Update an existing item by its ID.
    """
    try:
        updated_item = update_item_by_id_sv(db, item_id, item_data)
        return updated_item
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except UpdateError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Delete an item by ID
@router.delete("/{item_id}")
def delete_item_by_id(item_id: int, db: Session = Depends(get_db)):
    """
    Delete an item by its ID.
    """
    try:
        delete_item_sv(db, item_id)
        return {"message": "Item deleted successfully."}
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except DeleteError as e:
        raise HTTPException(status_code=400, detail=str(e))
