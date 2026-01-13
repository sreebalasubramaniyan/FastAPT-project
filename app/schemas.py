from pydantic import BaseModel

class PostCreate(BaseModel): #inherit the BaseModel class
    title: str
    content : str