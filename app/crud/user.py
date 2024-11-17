from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate
from app.utils.password_util import hash_password


# Get user by email
def get_user_by_email_db(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Create a new user
def create_user_db(db: Session, user_data: UserCreate):
    hashed_password = hash_password(user_data.password)
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Delete user by id
def delete_user_by_id_db(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
