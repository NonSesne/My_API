from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto") #used for hashing passwords
def hash_pwd(pwd:str):
    return pwd_context.hash(pwd)


def Check_Credentials(plane_password,hashed_password):
    return pwd_context.verify(plane_password,hashed_password)