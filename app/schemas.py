from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, Literal
# from pydantic.types import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = {
            "from_attributes": True
            }



class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    model_config = {
            "from_attributes": True
            }    

class PostOut(BaseModel):
    Post: Post
    votes: int

    model_config = {
            "from_attributes": True
            }

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    # dir: conint(ge=0, le=1)
    dir: Literal[0,1] # Restrict dir to only 0 or 1