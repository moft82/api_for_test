from sqlalchemy.orm import Session
from app.error.user import UserAlreadyExistsError
from app.schemas.user import UserCreate
from app.crud.user import create_user_db, delete_user_db, get_user_by_email_db

# Register a new user
def register_user_sv(db: Session, user_data: UserCreate):
    existing_user = get_user_by_email_db(db, user_data.email)
    if existing_user:
        raise UserAlreadyExistsError(user_data.email)
    
    return create_user_db(db, user_data)

# Service to delete a user by ID
def delete_user_sv(db: Session, user_id: int):
    success = delete_user_db(db, user_id)
    if not success:
        raise ValueError(f"User with ID {user_id} not found")
    return {"message": "User deleted successfully"}