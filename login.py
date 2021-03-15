from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

#Database
client = MongoClient('127.0.0.1', 27017)
db = client.user_login_system

#Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')