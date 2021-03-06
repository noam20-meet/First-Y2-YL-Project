from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key = True)
	full_name = Column(String)
	nickname = Column(String)
	password = Column(Integer)
	email = Column(String)
	