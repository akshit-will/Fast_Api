from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from typing import Literal

class PostBase(BaseModel):   # schema
    title : str
    content : str
    published : bool = True

class PostCreate(PostBase):
    pass

class User_Out(BaseModel):
    id : int
    email : EmailStr
    created_at: datetime 

    class Config:
        from_attributes = True

class Post(PostBase):

    created_at: datetime
    owner_id: int
    owner : User_Out
    id : int

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email : EmailStr
    password : str


class UserLogin(BaseModel):
    email : EmailStr
    password : str


class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: Literal[0, 1]

