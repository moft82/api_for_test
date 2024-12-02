from sqlalchemy.orm import Session
from app.db.models.item import Item
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate

# Get a item by ID
def get_items_db(db: Session) -> ItemResponse:
    return db.query(Item).all()

# Get all items belonging to a specific user by user_id
def get_item_by_id_db(db: Session, item_id: int):
    return  db.query(Item).filter(Item.id == item_id).fisrt()

# Create a new item
def create_item_db(db: Session, item_data: ItemCreate) -> ItemResponse:
    db.add(item_data)
    db.commit()
    db.refresh(item_data)
    return item_data

# Update an existing item
def update_item_db(db: Session, item: Item, item_data: ItemUpdate) -> ItemResponse:
    db.commit()
    db.refresh(item)  # Refresh to get updated fields
    return item

# Delete a item by ID
def delete_item_by_id_db(db: Session, item_id: int) -> bool:
    item = get_item_by_id_db(db, item_id)
    if item:
        db.delete(item)
        db.commit()
        return True
    return False
