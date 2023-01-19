from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

#Base schema for a post - makes a model for a post
class postBase(BaseModel):
    title: str
    content: str
    published: bool = True

#Schema for creating a post - same as postBase
class postCreate(postBase):
    pass

#Schema for updating a post - allows only certain values to be updated
class postUpdate(BaseModel):
    published: bool

#Schema for a user  - makes a model for a user
class userBase(BaseModel):
    password: str
    email: EmailStr

#Schema for updating a post - same as postUpdate
class userCreate(userBase):
    pass

#Schema for updating a post - allows only certain values to be updated
class userUpdate(userBase):
    pass

#Schema for user login
class userLogin(BaseModel):
    email: EmailStr
    password: str

class vote(BaseModel):
    post_id: int
    dir: conint(le=1)

#Response Schemas

#Schema for a user reponse
class user(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

#Schema for a post response - allows only certain data to be returned to the user
class Post(postBase):
    id: str
    created_at: datetime
    owner_id: int
    owner: user

    class Config:
        orm_mode = True

class postOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

#Schema for a token response 
class token(BaseModel):
    access_token: str
    token_type: str

#Schema for the token payload data
class tokenData(BaseModel):
    id: Optional[str] = None

