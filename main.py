from typing import Optional
from fastapi import FastAPI , Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):   # schema
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None

my_post = [{"title" : "title of post 1","content" : "content of post 1", "id" : 1},  # we done this to save the data because we
           {"title" : "favourate food" , "content" : "burger is my fav", "id" : 2}]  # are not using database currently

def find_post(id):
    for p in my_post:
        if(p["id"] == id):
            return p

@app.get("/")
def root():
    return {"message": "Welcome to my API!!!!!!"}

@app.get("/posts")
def get_post():
    return {"Data" : my_post}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post : Post):
    print(post)
    print(post.model_dump()) # .dict() = .model_dump()
      # {we can convert any pydantic model into dictionary by appling .model_dump()}
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0,100000000)
    my_post.append(post_dict)
    return {"Data":post_dict}      

@app.get("/posts/{id}")
def get_post(id: int,response : Response):
    post = find_post(id)
    if not post:
        # raise HTTPException(Status_code =status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'Message' : f"Post with id: {id} was not found"}
    return {"post_detail" : post}