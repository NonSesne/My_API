from passlib.context import CryptContext

#? used for hashing passwords
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto") 

def hash_pwd(pwd:str):
    return pwd_context.hash(pwd)


def Check_Credentials(plane_password,hashed_password):
    return pwd_context.verify(plane_password,hashed_password)