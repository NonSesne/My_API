from .. import schemas,utils,models,oauth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from ..data_base import get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List,Optional


router=APIRouter(prefix="/users",tags=["Users"])


@router.get("/",response_model=List[schemas.User_Out])
def get_users(db:Session=Depends(get_db)):
    users=db.query(models.User).all()
    return users


@router.post("/",response_model=schemas.User_Out,status_code=status.HTTP_201_CREATED)
def cerate_user(new_user_info:schemas.create_user,db:Session=Depends(get_db)):
    exist=db.query(models.User).filter(models.User.email==new_user_info.email).first()
    if exist!=None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    hashed_pwd= utils.hash_pwd(new_user_info.password)
    new_user=models.User(**new_user_info.model_dump())
    new_user.password=hashed_pwd
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",response_model=schemas.User_Public_Info)
def find_user(id:int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} was not found!")
    return user


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int,db:Session =Depends(get_db)):
    query=db.query(models.User).filter(models.User.id==id)
    
    if query.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    query.delete()
    db.commit()
    return {"DATA":"Success"}


@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED,response_model=schemas.User_Out)
def update_user (id:int,update_user_info:schemas.User_Public_Info,db: Session =Depends(get_db),Current_user:dict=Depends(oauth2.get_current_user)):
    query = db.query(models.User).filter(models.User.id==id)
    post=query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    query.update(update_user_info.model_dump())
    db.commit()
    return post

#! ADDING FOLLOWING SYSTEM !#
@router.post("/{id}/follow",status_code=status.HTTP_201_CREATED)
def follow(id:int, db : Session=Depends(get_db),Current_user:schemas.token_data=Depends(oauth2.get_current_user)):
    new_follow = models.followings(follower_id=Current_user.user_id,followed_id=id)
    db.add(new_follow)
    db.commit()
    return {"Data":"Followed !"}
        
@router.post("/{id}/unfollow",status_code=status.HTTP_201_CREATED)
def follow(id:int, db : Session=Depends(get_db),Current_user:schemas.token_data=Depends(oauth2.get_current_user)):
    query = db.query(models.followings).filter(models.followings.followed_id==id)
    action = query.first()
    if(action==None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    query.delete()
    db.commit()
    return {"Data":"Unollowed !"}