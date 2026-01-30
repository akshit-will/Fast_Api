from fastapi import FastAPI , Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from typing import List

router = APIRouter(
   prefix="/posts",
    tags=["Posts"]
)

@router.get("/",response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    return posts

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post : schemas.PostCreate,db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING
    #                 *""",(post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    # print(post)
    # print(post.model_dump()) # .dict() = .model_dump()
    #   # {we can convert any pydantic model into dictionary by appling .model_dump()}
    # post_dict = post.model_dump()
    # post_dict['id'] = randrange(0,100000000)
    # my_post.append(post_dict)
    return new_post

@router.get("/{id}",response_model=schemas.Post)
def get_post(id: int,db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    # cursor.execute("""SELECT * FROM posts WHERE id =%s """,(str(id),))
    # post = cursor.fetchone()
    # post = find_post(id)
    if not post:
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,
                             detail=f"Post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Message' : f"Post with id: {id} was not found"}
    return post
   


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
 # delete post
 # find the index in the array that has required ID
 # my_post,pop(index)
#  index = find_index_post(id)
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
     raise HTTPException(status_code =status.HTTP_404_NOT_FOUND, 
                         detail=f"Post with id: {id} was not found")
    post.delete(synchronize_session=False)
    db.commit()
#  my_post.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Post)
def update_post(id: int,updated_post : schemas.PostCreate,db: Session = Depends(get_db)):
    #  cursor.execute("""UPDATE posts SET title = %s, content = %s,published = %s WHERE id = %s
    #                  RETURNING *""",(post.title,post.content,post.published, str(id)))
    #  updated_post = cursor.fetchone()
    #  conn.commit()
    #  index = find_index_post(id)
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
      raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,
                           detail=f"Post with id: {id} was not found")

    post_query.update(updated_post.model_dump(),synchronize_session=False)
    db.commit()

    #  post_dict = post.model_dump()
    #  post_dict["id"] = id
    #  my_post[index] = post_dict
    return post_query.first()