"""
model.py - interface to DB
"""

# ORG CODE from flask.ext.sqlalchemy import SQLAlchemy
# ORG CODE from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from werkzeug import generate_password_hash, check_password_hash

# ORG CODE db = SQLAlchemy()
# inherit features from sqlalchemy classes that correspond to tables in DB
Base = declarative_base()

# OOP representation of tables in DB
class User(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key = True)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(120), unique = True)
    pwdhash = Column(String(54))

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)


