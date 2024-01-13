from .. import schemas,models,oauth2
from fastapi import status,HTTPException,Depends,APIRouter
from ..data_base import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List,Optional
from sqlalchemy import func

router=APIRouter(prefix="/posts",tags=["Posts"])


@router.get("/",response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
 
    posts = db.query(models.Post, func.count(models.Up.post_id).label("Up"),func.count(models.Down.post_id).label("Down")).outerjoin(
        models.Up, models.Up.post_id == models.Post.id).outerjoin(models.Down,models.Down.post_id==models.Post.id).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    res_posts = []
    for post,Up,Down in posts:
        res_posts.append({
            "post": post,
            "up" : Up,
            "down": Down
        })
    return res_posts
    
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post(new_post_info: schemas.Create_post,db:Session=Depends(get_db),Token_info:schemas.token_data=Depends(oauth2.get_current_user)):
    new_post=models.Post(**new_post_info.model_dump())
    new_post.owner_id = Token_info.user_id
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}",response_model=schemas.PostOut)
def find_post(id:int,db:Session =Depends(get_db),Token_info:schemas.token_data=Depends(oauth2.get_current_user)):
    post = db.query(models.Post, func.count(models.Up.post_id).label("Up"),func.count(models.Down.post_id).label("Down")).outerjoin(
        models.Up, models.Up.post_id == models.Post.id).outerjoin(models.Down,models.Down.post_id==models.Post.id).group_by(models.Post.id).filter(models.Post.id==id).first()
    if post !=None:
        res_posts={"post":post[0],"up":post[1],"down":post[2]}
        return res_posts
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{id}",status_code=status.HTTP_201_CREATED,response_model=schemas.Post_base)
def update_post(id: int,updat_post_info:schemas.Post_base,db: Session=Depends(get_db),Token_info:dict=Depends(oauth2.get_current_user)):
    query=db.query(models.Post).filter(models.Post.id==id)
    post=query.first()
    if post!=None:
        if(Token_info.user_id != post.owner_id):
             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        query.update(updat_post_info.model_dump())
        db.commit()
        db.refresh(query.first())
        return query.first()
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)




@router.delete("/{id}",status_code=status.HTTP_200_OK)
def delete_post(id:int,db: Session=Depends(get_db),Token_info:dict=Depends(oauth2.get_current_user)):
    query = db.query(models.Post).filter(models.Post.id==id)
    post=query.first()
    if post!=None:
        if(Token_info.user_id != post.owner_id):
             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        query.delete()
        db.commit()
        return {"DATA":"Success"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)




@router.get("/{id}/Ups",response_model=list[schemas.reaction_out])
def get_Ups(id:int,db : Session =Depends(get_db)):
    query=db.query(models.Up).filter(models.Up.post_id==id)
    return query.all()



@router.get("/{id}/Downs",response_model=list[schemas.reaction_out])
def get_Downs(id:int,db : Session =Depends(get_db)):
    query=db.query(models.Down).filter(models.Down.post_id==id)
    return query.all()