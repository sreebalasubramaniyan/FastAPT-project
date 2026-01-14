
from fastapi import FastAPI , HTTPException, File,UploadFile,Depends
from  app.schemas import PostCreate
# importing our database
from app.db import Post,create_db_and_tables,get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import  asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield



# creating an object
app = FastAPI(lifespan=lifespan)
# get(endpoint/path)

#1)creating simple end point

# @app.get("/hello-world") # @ is decorator
# def hello_world():
#     return {"message":"Hello World"} # data/JSON - pydantic or python dictionary

#2)creating text_post endpoint

text_posts = {
    1: {
        "title": "New Post",
        "content": "cool test post"
    },
    2: {
        "title": "Learning FastAPI",
        "content": "FastAPI is fast and easy to use"
    },
    3: {
        "title": "Python Tips",
        "content": "Use list comprehensions for cleaner code"
    },
    4: {
        "title": "Backend Basics",
        "content": "APIs connect frontend and backend"
    },
    5: {
        "title": "REST API",
        "content": "REST uses HTTP methods like GET and POST"
    },
    6: {
        "title": "Databases",
        "content": "SQL databases store structured data"
    },
    7: {
        "title": "Authentication",
        "content": "JWT is commonly used for securing APIs"
    },
    8: {
        "title": "Error Handling",
        "content": "Always return proper HTTP status codes"
    },
    9: {
        "title": "Projects",
        "content": "Build projects to learn faster"
    },
    10: {
        "title": "Deployment",
        "content": "Deploy APIs using cloud platforms"
    }
}

# get all posts
@app.get("/posts")
# query paramter with default value
def get_all_posts(limit:int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts
# get individual post with their id
@app.get("/posts/{id}")
# in function also id has to be given
def get_post_by_id(id:int):
    # want to return an error
    # if id is not in the posts
    # 1) import HTTPException
    # 2) raise the error

    if id not in text_posts:
        # HTTPException(status_code,details)
        raise HTTPException(404,"post not found")
    return text_posts[id]


# 3) learn about queries parameters basics
    """
    def get_all_posts(limit:int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts
    """

#4 ) learn about post endpoint
# for best documentation we gonna mention the each data type
@app.post("/posts")
def create_post(post:PostCreate)->PostCreate: # for sending a data we gonna learn new thing called schema
    # using requestBody 
        # body is kinda hidden info
        # creating schema we can acces that body

    new_post = {"title":post.title,"content":post.content}
    new_id = max(text_posts.keys())+1
    # FastAPI automaticaly consider post.title as a string
    text_posts[new_id] = new_post
    # return new_post as the response
    return new_post

