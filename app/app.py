from fastapi import FastAPI 
# creating an object
app = FastAPI()
# get(endpoint/path)


#1)creating simple end point
# @app.get("/hello-world") # @ is decorator
# def hello_world():
#     return {"message":"Hello World"} # data/JSON - pydantic or python dictionary

#2)creating text_post endpoint

text_posts = {
    1 : {
        "title" : "New Post",
        "content" : "cool test post"
       }
}
# get all posts
@app.get("/posts")
def get_all_posts():
    return text_posts
# get individual post with their id
@app.get("/posts/{id}")
# in function also id has to be given
def get_post_by_id(id:int):
    return text_posts[id]