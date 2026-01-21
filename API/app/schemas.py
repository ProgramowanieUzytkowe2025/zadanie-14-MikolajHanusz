from pydantic import BaseModel
from typing import Optional

class MebelBase(BaseModel):
    nazwa:str
    cena:Optional[int] = None
    kupione:Optional[bool] = None

class MebelCreate(MebelBase):
    pass

class MebelUpdate(BaseModel):
    nazwa:Optional[str] = None
    cena:Optional[int] = None
    kupione:Optional[bool] = None

class MebelOut(MebelBase):
    id:int

class Config:
    orm_mode = True