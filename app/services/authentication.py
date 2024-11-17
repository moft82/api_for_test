import jwt
from datetime import timedelta
from typing import Optional
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.crud.user import get_user_by_email_db
from app.utils.password_util import verify_password
from app.core.config import config
from app.utils.time_util import get_KST

# Load params form Config
SECRET_KEY = config.SECRET_KEY
ALGORITHM = config.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = config.ACCESS_TOKEN_EXPIRE_MINUTES  

# Authenticate user by verifying email and password
def authenticate_user_sv(db: Session, email: str, password: str):
    user = get_user_by_email_db(db, email)
    if user and verify_password(password, user.hashed_password): 
        return user
    return None

# Generate JWT token for authenticated user
def create_token_for_user_sv(user: User):
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token_sv(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return access_token

# Create a JWT token
def create_access_token_sv(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = get_KST() + expires_delta
    else:
        expire = get_KST() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Verify and decode JWT token
def verify_access_token_sv(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
