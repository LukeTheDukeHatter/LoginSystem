from Datastore import DataStore
from Messenger import MailServer
from flask import Flask, redirect, request, render_template

import keys


Database    = DataStore('Main')
EmailServer = MailServer('Luuke 2FA', keys.Email, keys.Password)
app         = Flask(__name__)

@app.route('/', methods=['GET'])
def Catchall():
	return redirect('/login')

@app.route('/home', methods=['GET'])
def home():
	return open('home.html').read()

@app.route('/login', methods=['GET', 'POST'])
def Login():
	if request.method == 'GET':
		return open('Login.html').read()
	else:
		if Database.GetLogin(request.form['Email']) == False:
			return 'Login Failed'
		else:
			if Database.GetLogin(request.form['Email']).CheckLogin(request.form['Password']):
				return 'Login Successful'
			else:
				return 'Login Failed'

@app.route('/validate', methods=['GET', 'POST'])
def Validate():
	if request.method == 'GET':
		return open('CodeEntry.html').read().replace("{EmailReplace}", request.args['Email'])
	else:
		if Database.GetLogin(request.form['Email']):
			return 'Email Already Exists'
		else:
			Database.AddLogin(request.form['Email'], request.form['Username'], request.form['Password'])
			return 'Registration Successful'

@app.route('/register', methods=['GET', 'POST'])
def Register():
	if request.method == 'GET':
		return open('Signup.html').read()
	else:
		if Database.GetLogin(request.form['Email']):
			return 'Email Already Exists'
		else:
			Database.AddLogin(request.form['Email'], request.form['Username'], request.form['Password'])
			return 'Registration Successful'

@app.route('/robots.txt')
def robots(): 
	return 'User-agent: *\nDisallow: /'

app.run()