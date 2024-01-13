from .. import schemas,utils,models,oauth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from ..data_base import get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix="/react",tags=['Reactions'])



@router.get("/{id}/Up",status_code=status.HTTP_201_CREATED)
def react(id:int, db : Session= Depends(get_db),Token_info:schemas.token_data = Depends(oauth2.get_current_user)):

    if db.query(models.Post).filter(models.Post.id==id).first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    Reaction_query= db.query(models.Up).filter(models.Up.post_id==id,models.Up.user_id==Token_info.user_id)
    Reaction=Reaction_query.first()
    if Reaction!=None :
        Reaction_query.delete(synchronize_session=False)
        db.commit()
        return {"Data":"Successfully removed!"}
    else :
        Reaction_query= db.query(models.Down).filter(models.Down.post_id==id,models.Down.user_id==Token_info.user_id)
        if Reaction_query.first()!=None:
            Reaction_query.delete(synchronize_session=False)
        new_Reaction= models.Up(post_id=id,user_id=Token_info.user_id)
        db.add(new_Reaction)
        db.commit()
        return {"Data":"Succefully Liked"}



@router.get("/{id}/Down",status_code=status.HTTP_201_CREATED)
def Down(id:int,db : Session= Depends(get_db),Token_info:schemas.token_data=Depends(oauth2.get_current_user)):
    if db.query(models.Post).filter(models.Post.id==id).first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    Reaction_query= db.query(models.Down).filter(models.Down.post_id==id,models.Down.user_id==Token_info.user_id)
    Reaction=Reaction_query.first()
    if Reaction!=None :
        Reaction_query.delete(synchronize_session=False)
        db.commit()
        return {"Data":"Successfully removed!"}
    else :
        Reaction_query= db.query(models.Up).filter(models.Up.post_id==id,models.Up.user_id==Token_info.user_id)
        if Reaction_query.first()!=None:
            Reaction_query.delete(synchronize_session=False)
        new_Reaction= models.Down(post_id=id,user_id=Token_info.user_id)
        db.add(new_Reaction)
        db.commit()
        return {"Data":"Succefully Disliked"}
 
