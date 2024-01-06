from .data_base import Base
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
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
    likes = Column(Integer)
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

    #is it possible that someday your are gonna do a game dev stream or just programming stuff? cuz i really liked the tutorials tbh.


class Reactions(Base):
    __tablename__="reactions"
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)