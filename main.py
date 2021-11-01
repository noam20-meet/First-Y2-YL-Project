from database import *
from flask import Flask, request, redirect, render_template
from flask import session as login_session
from model import *

# <link rel="stylesheet" href="*LINK*">

app = Flask(__name__,template_folder='template')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/mainpage')
def mainpage():
	return render_template('mainpage.html')	

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	else:
		full_name = request.form['full_name']
		nickname = request.form['nickname']
		password = request.form['password']
		email = request.form['email']
		add_user(full_name, nickname, password, email)
		return render_template('home.html')
		
@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
	  return render_template("login.html")
	else:
		nickname = request.form['nickname']
		password = request.form['password']
		user = query_by_name(nickname)
		if user != None:
			if password == user.password:
				return render_template('mainpage.html')
			else:
				return render_template('login.html')
		else:
			return render_template('login.html')
     
#write your code here!
if __name__ == "__main__":
	app.run(
		host='0.0.0.0',
		debug=True
	)