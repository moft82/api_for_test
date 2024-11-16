import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import db
from app.crud.user import get_user_by_email
from app.services.authentication import verify_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Dependency to extract email from token and get user from database
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(db.get_db)):
    try:
        payload = verify_access_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = get_user_by_email(db, email)
        
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        return user
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))