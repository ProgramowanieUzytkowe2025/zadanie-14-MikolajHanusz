from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.databse import SessionLocal, init_db
from app.modelMebel import Mebel
from app.schemas import MebelCreate, MebelUpdate, MebelOut
from fastapi.middleware.cors import CORSMiddleware


# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB tables on startup
@app.on_event("startup")
def startup():
    init_db()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------
# CRUD functions
# ----------------------
def get_mebel(db: Session, mebel_id: int):
    return db.query(Mebel).filter(Mebel.id == mebel_id).first()

def get_meble(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Mebel).order_by(Mebel.id).offset(skip).limit(limit).all()

def create_mebel(db: Session, mebel: MebelCreate):
    db_obj = Mebel(**mebel.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_mebel(db: Session, db_obj: Mebel, update: dict):
    for field, value in update.items():
        if value is not None:
            setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_mebel(db: Session, db_obj: Mebel):
    db.delete(db_obj)
    db.commit()


# ----------------------
# Endpoints
# ----------------------
@app.get("/mebel", response_model=List[MebelOut])
def read_meble(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_meble(db, skip, limit)

@app.get("/mebel/{mebel_id}", response_model=MebelOut)
def read_mebel(mebel_id: int, db: Session = Depends(get_db)):
    db_obj = get_mebel(db, mebel_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Mebel not found")
    return db_obj

@app.post("/mebel", response_model=MebelOut, status_code=201)
def create_mebel_endpoint(mebel: MebelCreate, db: Session = Depends(get_db)):
    return create_mebel(db, mebel)

@app.put("/mebel/{mebel_id}", response_model=MebelOut)
def update_mebel_endpoint(mebel_id: int, mebel: MebelUpdate, db: Session = Depends(get_db)):
    db_obj = get_mebel(db, mebel_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Mebel not found")
    return update_mebel(db, db_obj, mebel.dict(exclude_unset=True))

@app.delete("/mebel/{mebel_id}", status_code=204)
def delete_mebel_endpoint(mebel_id: int, db: Session = Depends(get_db)):
    db_obj = get_mebel(db, mebel_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Mebel not found")
    delete_mebel(db, db_obj)
