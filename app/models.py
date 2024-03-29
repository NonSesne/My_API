from .data_base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Post(Base):
    __tablename__="posts"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    publiched= Column(Boolean,server_default='True')
    created_at = Column(TIMESTAMP(timezone=True),server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner = relationship ("User")


class User(Base):
    __tablename__="users"
    id =Column(Integer,primary_key=True)
    username = Column(String,nullable=False,unique=False)
    email = Column(String,nullable=False,unique=True)
    password= Column(String,nullable=False,unique=False)
    created_at = Column(TIMESTAMP(timezone=True),server_default=text('now()'))
    bio = Column(String(length=256),nullable=True)
    phone_number = Column(String(length=12),nullable=True)
    first_name = Column(String(length=12),nullable=True)
    last_name = Column(String(length=12),nullable=True)
    

    #is it possible that someday your are gonna do a game dev stream or just programming stuff? cuz i really liked the tutorials tbh.


class Up(Base):
    __tablename__="Up"
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    user = relationship("User")

class Down(Base):
    __tablename__="Down"
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    user = relationship("User")

#! Following System !#

class followings(Base):
    __tablename__="followings"
    follower_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False,primary_key=True)
    followed_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False,primary_key=True)
    follower = relationship("User",foreign_keys=follower_id)
    followed = relationship("User",foreign_keys=followed_id)

