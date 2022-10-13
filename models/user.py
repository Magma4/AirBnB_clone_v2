#!/usr/bin/python3
# File: user.py
# Main Authors: Justin Majetich - Ezra Nobrega
# email(s): <justinmajetich@gmail.com>
#           <ezra.nobrega@outlook.com>
# Collaborators: Yoshua Lopez - Ma Paz Quirola - Laura Socarras
#           
"""This module defines a class User"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    password = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    first_name = Column(
        String(128), nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    last_name = Column(
        String(128), nullable=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
        'Place',
        cascade="all, delete, delete-orphan",
        backref='user'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    reviews = relationship(
        'Review',
        cascade="all, delete, delete-orphan",
        backref='user'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
