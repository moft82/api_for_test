import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import db
from app.crud.user import get_user_by_email_db
from app.services.authentication import verify_access_token_sv


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Dependency to extract email from token and get user from database
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(db.get_db)):
    try:
        payload = verify_access_token_sv(token)
        email: str = payload.get("sub")
        if email is None:
            print("Email is missing in the token payload")
            raise HTTPException(status_code=401, detail="Invalid token")
        user = get_user_by_email_db(db, email)
        
        if user is None:
            print("User not found in the database")
            raise HTTPException(status_code=404, detail="User not found")
        
        return user
    
    except jwt.ExpiredSignatureError:
        print("Token has expired")
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        print("Invalid token")
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        print(f"Error in get_current_user: {e}")
        raise HTTPException(status_code=403, detail=str(e))