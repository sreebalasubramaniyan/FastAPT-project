from pydantic import BaseModel
# this is called requestBODY
class PostCreate(BaseModel): #inherit the BaseModel class
    title: str
    content : str