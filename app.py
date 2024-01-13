from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/login')
def login():
    return 'login success'

@app.route('/profile/<username>')
def profile(username):
    return {'username': username}

@app.route('/index')
def test():
    return render_template('index.html')