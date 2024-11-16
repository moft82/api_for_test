from sqlalchemy.orm import Session
from app.db.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

# Get a item by ID
def read_all_items_db(db: Session) -> Item:
    return db.query(Item).all()

# Get all items belonging to a specific user by user_id
def read_items_by_user_id_db(db: Session, user_id: int):
    items = db.query(Item).filter(Item.user_id == user_id).all()
    if not items:
        raise ValueError(f"No items found for user with ID {user_id}")
    return items


def read_item_by_id_and_user_db(db: Session, item_id: int, user_id: int) -> Item:
    item = db.query(Item).filter(Item.id == item_id, Item.user_id == user_id).first()
    if not item:
        raise ValueError(f"No items found for user with User Id {user_id} and item Id: {item_id}")
    
    return item

# Create a new item
def create_item_db(db: Session, new_item: ItemCreate) -> Item:
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# Update an existing item
def update_item_db(db: Session, item: Item, item_data: ItemUpdate) -> Item:
    if item_data.title:
        item.title = item_data.title
    if item_data.description:
        item.description = item_data.description
    
    db.commit()
    db.refresh(item)  # Refresh to get updated fields
    return item

# Delete a item by ID
def delete_item_db(db: Session, item_id: int, user_id: int) -> bool:
    item = db.query(Item).filter(Item.id == item_id, Item.user_id == user_id).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    return False
