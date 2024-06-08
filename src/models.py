import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

class Login(Base):
    __tablename__ = 'login'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    mail = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    user_id_for_login = Column(Integer, ForeignKey('user.id'))
    user_for_login = relationship(User)

    def to_dict(self):
        return {}
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    favorite_character = Column(String(250),nullable=False)
    favorite_planet = Column(String(250),nullable=False)

    
class Character(Base):
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    favorite = relationship(Favorites)

class PLanets(Base):
    __tablename__='planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    population = Column(String(250))
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    favorite = relationship(Favorites)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
