from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from passlib.hash import pbkdf2_sha256
from flask_cors import CORS
from config import BaseConfig
from mongoengine import *

app = Flask(__name__)
app.config.from_object(BaseConfig)
user_db = MongoEngine(app)
CORS(app)

class User(Document):
    name		= StringField(max_length=255, required=True)
    email		= StringField(max_length=255, unique=True)
    password	= StringField(max_length=255, required=True)

@app.route("/api/login", methods=["POST"])
def login():  
    try:
        email = request.json["email"]
        password = request.json["password"]
        user = User.objects.get(email=email)

        if user and pbkdf2_sha256.verify(password, user['password']):
            return jsonify(True)
        else:
            return jsonify({"error": "Incorrect Password"})
        return jsonify({"success": True})
    except DoesNotExist:
        return jsonify({"error": "Entered email is not associated with a user"})
    

@app.route("/api/register", methods=["POST"])
def register():
    try:
        email = request.json["email"].lower()
        password_encrypted = pbkdf2_sha256.encrypt(request.json["password"])
        name = request.json["name"]
        # Check to see if user already exists
        try:
            new_user = User(name=name, email=email, password=password_encrypted)
            new_user.save()
        except user_db.NotUniqueError:
            return jsonify({"error": "User with that email already exists"}) #, 409
        return jsonify({"success": True})
    except:
        return jsonify({"error": "Invalid form"})
    
    


if __name__ == "__main__":
    app.run(debug=True) # debug=True restarts the server everytime we make a change in our code