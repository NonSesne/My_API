from typing import Optional
from pydantic import BaseModel,EmailStr
from datetime import datetime

class Post_base(BaseModel):
    title : str
    content: str
    publiched: bool = True
    
class Create_post(Post_base):
    pass


class User_Out(BaseModel):
    id:int
    username:str
    email:EmailStr

class Post(Post_base):
    id: int
    created_at: datetime
    owner : User_Out
  


class PostOut(BaseModel):
    post : Post
    up : int
    down:int


class create_user(BaseModel):
    username:str
    email : EmailStr
    password : str


class User_Public_Info(BaseModel):
    username:str
    email:EmailStr




class User_login(BaseModel):
    email : EmailStr
    password : str


class Token(BaseModel):
    Access_Token:str
    Token_Type:str


class token_data(BaseModel):
    user_id : Optional[int] = None
    username : Optional[str] = None


class react_data(BaseModel):
    post_id: int

