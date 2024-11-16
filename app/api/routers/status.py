from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.db.database import db
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.db.models.status import Status as StatusModel
from app.schemas.status import StatusCreate, Status as StatusSchema

router = APIRouter(
    prefix="/status",
    tags=["status"],
    responses={404:{"description" : "Not Found"}}
)

# Create a Jinja2Templates instance
templates = Jinja2Templates(directory="app/templates")

@router.post("/", response_model = StatusSchema)
def create_status(item: StatusCreate, db: Session = Depends(db.get_db)):
    db_item = StatusSchema(**item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/read_all_items")
def read_all_item(db: Session = Depends(db.get_db)):
    data = db.query(StatusModel).all()
    if data is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"data":data}

@router.get("/")
def main(request:Request):
    # Define Status
    available_status = ["a", "b"]
    selectable_status = available_status + ["c"]

    return templates.TemplateResponse("status.html", {"request" : request, "available_status":available_status, "selectable_status":selectable_status})

@router.put("/{item_id}", response_model = StatusSchema)
def update(item_id:int, item: StatusCreate, db: Session = Depends(db.get_db)):
    db_item = db.query(StatusModel).filter( StatusModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.status = item.status
    db.commit()
    return db_item

# @router.get("/{id}", response_model=StatusSchema)
# def read_item(id: int, db: Session = Depends(dataBase.get_db)):
#     db_item = db.query(StatusModel).filter(StatusModel.id == id).first()
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return db_item