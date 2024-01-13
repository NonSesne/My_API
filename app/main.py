from fastapi import FastAPI
from .routers import Post_file,User_file,auth_file,React_file,follow_file
from fastapi.middleware.cors import CORSMiddleware

#? models.Base.metadata.create_all(bind=engine)
#! Alembic did this work


origins = ['https://www.google.com']


app=FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Post_file.router)
app.include_router(User_file.router)
app.include_router(auth_file.router)
app.include_router(React_file.router)
app.include_router(follow_file.router)


@app.get("/",status_code=404)
def get_nothing():
        return {"Data":"Nothing"}        
