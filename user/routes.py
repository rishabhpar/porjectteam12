from flask import Flask
from login import app
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()
