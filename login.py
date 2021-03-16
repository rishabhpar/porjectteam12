from flask import Flask, render_template, session, redirect
from functools import wraps
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = b'\xda\xba[\x7f\xa4\xbe\x0ce8\xde>*#6"='

#Database
client = MongoClient('127.0.0.1', 27017)
db = client.user_login_system

# Wrapper to require login to access the dashboard
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap

#Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')