from .. import schemas,models,oauth2
from fastapi import status,HTTPException,Depends,APIRouter
from ..data_base import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(prefix="/users",tags=["follow"])

#! ADDING FOLLOWING SYSTEM !#



@router.get("/{id}/follow",status_code=status.HTTP_201_CREATED)
def follow(id:int, db : Session=Depends(get_db),Current_user:schemas.token_data=Depends(oauth2.get_current_user)):
    query = db.query(models.followings).filter(models.followings.followed_id==id).filter(models.followings.follower_id==Current_user.user_id)
    action = query.first()
    if(action!=None):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    new_follow = models.followings(follower_id=Current_user.user_id,followed_id=id)
    db.add(new_follow)
    db.commit()
    return {"Data":"Followed !"}




@router.get("/{id}/unfollow",status_code=status.HTTP_201_CREATED)
def follow(id:int, db : Session=Depends(get_db),Current_user:schemas.token_data=Depends(oauth2.get_current_user)):
    query = db.query(models.followings).filter(models.followings.followed_id==id).filter(models.followings.follower_id==Current_user.user_id)
    action = query.first()
    if(action==None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    query.delete()
    db.commit()
    return {"Data":"Unfollowed !"}




@router.get("/{id}/followers",response_model=List[schemas.follower_Out])
def get_followers(id:int,db: Session = Depends(get_db)):
    query = db.query(models.followings).filter(models.followings.followed_id==id)
    return query.all()



@router.get("/{id}/following",response_model=List[schemas.following_Out])
def get_followers(id:int,db: Session = Depends(get_db)):
    query = db.query(models.followings).filter(models.followings.follower_id==id)
    return query.all()