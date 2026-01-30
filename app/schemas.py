from pydantic import BaseModel,EmailStr
from datetime import datetime

class PostBase(BaseModel):   # schema
    title : str
    content : str
    published : bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):

    created_at: datetime
    id : int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class User_Out(BaseModel):
    id : int
    email : EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email : EmailStr
    password : str