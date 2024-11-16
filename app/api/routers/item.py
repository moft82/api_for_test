from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.dependecies.authentication import get_current_user
from app.dependecies.database import get_db
from app.services.item import create_item_sv, delete_item_sv, read_all_items_sv, read_item_by_id_and_user_id_sv, read_items_by_user_id_sv, update_item_sv

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404:{"description" : "Not Found"}}
)

@router.get("/", response_model=list[ItemResponse])
def read_all_items(db: Session = Depends(get_db)):
    items = read_all_items_sv(db = db)
    return items

@router.get("/user", response_model=list[ItemResponse])
def read_items_by_user_id(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    items = read_items_by_user_id_sv(db = db, user_id = user.id)
    return items


@router.get("/{item_id}", response_model=ItemResponse)
def read_by_item_id(item_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    item = read_item_by_id_and_user_id_sv(db=db, item_id=item_id, user_id=user.id)
    return item

@router.post("/", response_model = ItemResponse)
def create_item(item: ItemCreate, file:UploadFile, db: Session = Depends(get_db), user:User = Depends(get_current_user)):
    item = create_item_sv(db=db, item_data =item, file=file, user_id = user.id)
    return item

@router.put("/{item_id}", response_model = ItemResponse)
def update_item(item_id:int, item_update: ItemUpdate, db: Session = Depends(get_db), user:User = Depends(get_current_user)):
    try:
        return update_item_sv(db, item_id, item_update)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delect("/{item_id}")
def delete_item(item_id:int, db: Session = Depends(get_db), user:User = Depends(get_current_user)):
    try:
        delete_item_sv(db, item_id, user.id)
        return {"message": "Project deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


