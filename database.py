from model import Base, Users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///person.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(full_name, password, email, nickname):
	user = Users(full_name = full_name, nickname = nickname, password = password , email = email)
	 
	session.add(user)
	session.commit()

def delete_user(id):
  session.query(Users).filter_by(id=id).delete()

def query_by_name(full_name):
  user = session.query(Users).filter_by(username = full_name).first()
  return user