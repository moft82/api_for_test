from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.dependecies.authentication import get_current_user
from app.dependecies.database import get_db
from app.schemas.authentication import LoginRequest, TokenResponse
from app.schemas.user import UserCreate
from app.services.authentication import authenticate_user_sv, create_token_for_user_sv
from app.services.user import delete_user_sv, register_user_sv

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404:{"description" : "Not Found"}}
)

# Route for user registration
@router.post("/register")
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = register_user_sv(db, user_data)
        return {"message": "User registered successfully", "name": new_user.name}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route for log in
@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user_sv(db, request.email, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = create_token_for_user_sv(user)
    return {"access_token": access_token, "token_type": "bearer"}

# Delete user
@router.delete("/")
def delete_user_by_id(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user_id = user.id
    try:
        delete_user_sv(user_id, db)
        return {"message": "User deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))