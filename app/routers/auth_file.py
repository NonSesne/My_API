from .. import schemas,utils,models,oauth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from ..data_base import get_db
from sqlalchemy.orm import Session
from typing import List

router=APIRouter(tags=["Authentication"])


@router.post("/login",status_code=status.HTTP_202_ACCEPTED,response_model=schemas.Token)

def login(user_credentials: schemas.User_login , db: Session=Depends(get_db)):

    this_user = db.query(models.User).filter(models.User.email==user_credentials.email).first()
    if this_user == None or not utils.Check_Credentials(user_credentials.password,this_user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Invalid credentianls!")
    
    Access_Token=oauth2.Create_Access_Token(data={"user_id":this_user.id,"username":this_user.username})

    return {"Access_Token" : Access_Token , "Token_Type":"bearer" }
