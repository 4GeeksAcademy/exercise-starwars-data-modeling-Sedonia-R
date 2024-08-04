import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}
    
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

# class Favorites(Base):
#     __tablename__ = "favorites"
#     id = Column(Integer, primary_key=True)
#     user_id = (Integer, ForeignKey('user.id'))
#     user = relationship(User)
#     planets_id = (Integer, ForeignKey('planets.id'))
#     characters_id = (Integer, ForeignKey('characters.id'))
#     vehicles_id = (Integer, ForeignKey('vehicles.id'))

#     def to_dict(self):
#         return {}
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    url = Column(String(1000), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    name = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    url = Column(String(1000), nullable=False)
    name = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    url = Column(String(1000), nullable=False)
    name = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    crew = Column(Integer, nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True) 

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
