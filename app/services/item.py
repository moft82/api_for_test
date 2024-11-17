from app.error.item import DeleteError, ItemCreateError, ItemNotFoundError, UpdateError
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.crud.item import create_item_db, delete_item_by_id_db, get_item_by_id_db, get_items_db, update_item_db
from app.core.logging_config import logger  # Import logger

# GET: Retrieve all items
def get_items_sv(db: Session) -> list[ItemResponse]:
    try:
        items = get_items_db(db)
        if not items:
            raise ItemNotFoundError("No items found.")
        return items
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemyError in get_items_sv: {str(e)}", exc_info=True)
        raise


# GET: Retrieve an item by ID
def get_item_by_id_sv(db: Session, item_id: int) -> ItemResponse:
    try:
        item = get_item_by_id_db(db, item_id)
        if not item:
            raise ItemNotFoundError(f"Item with ID {item_id} not found.")
        return item
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemyError in get_item_by_id_sv for ID {item_id}: {str(e)}", exc_info=True)
        raise


# POST: Create a new item
def create_new_item_sv(db: Session, item_data: ItemCreate) -> ItemResponse:
    try:
        return create_item_db(db, item_data)
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemyError in create_new_item_sv: {str(e)}", exc_info=True)
        raise


# PUT: Update an item by ID
def update_item_by_id_sv(db: Session, item_id: int, item_data: ItemUpdate) -> ItemResponse:
    existing_item = get_item_by_id_db(db, item_id)
    if not existing_item:
        raise ItemNotFoundError(f"Item with ID {item_id} not found.")

    updated_fields = item_data.dict(exclude_unset=True)
    if not updated_fields:
        raise UpdateError(item_id, "No valid fields provided to update.")

    try:
        for key, value in updated_fields.items():
            setattr(existing_item, key, value)
        updated_item = update_item_db(db, existing_item)
        return updated_item
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemyError in update_item_by_id_sv for ID {item_id}: {str(e)}", exc_info=True)
        raise


# DELETE: Delete an item by ID
def delete_item_sv(db: Session, item_id: int) -> bool:
    item = get_item_by_id_db(db, item_id)
    if not item:
        raise ItemNotFoundError(f"Item with ID {item_id} not found.")

    try:
        result = delete_item_by_id_db(db, item_id)
        if not result:
            raise DeleteError(item_id, "Failed to delete the item.")
        return result
    except SQLAlchemyError as e:
        logger.error(f"SQLAlchemyError in delete_item_sv for ID {item_id}: {str(e)}", exc_info=True)
        raise
