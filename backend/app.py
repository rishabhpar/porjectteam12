from flask import Flask, request, jsonify
# mongoengine is the package we will use to interact with MongoDB
# mongoengine is a little more structured than pymongo 
from flask_mongoengine import MongoEngine
# passlib is the package we will use to encrypt passwords
from passlib.hash import pbkdf2_sha256
# cors is used to relax security, only for development
from flask_cors import CORS
# vanilla mongoengine is used to format the schema of a users' acct info
from mongoengine import *
# import class from config.py
from config import BaseConfig

# create a Flask app
app = Flask(__name__)
app.config.from_object(BaseConfig)
CORS(app)

# create a database to host user information
user_db = MongoEngine(app)

# create a schema to organize what information we expect to have
# when hosting user information in the database: Name, Email, Password
class User(Document):
    name		= StringField(max_length=255, required=True)
    email		= StringField(max_length=255, unique=True)  # only one account for email
    password	= StringField(max_length=255, required=True)

# route to log in to the application
# we can only POST to the API
@app.route("/api/login", methods=["POST"])
def login():  
    try:
        # extract information from the submission form
        email = request.json["email"]
        password = request.json["password"]

        # check for an existing user's email in the database
        user = User.objects.get(email=email)

        # if a user exists and the password entered in the form
        # matches, this is a successful login; else, it is an error
        # so we send back feedback
        if user and pbkdf2_sha256.verify(password, user['password']):
            return jsonify({"success": True})
        else:
            return jsonify({"error": "Incorrect Password"})
    except DoesNotExist:
        # if a user with entered email does not exist, send a feedback message
        return jsonify({"error": "Entered email is not associated with a user"})
    

@app.route("/api/register", methods=["POST"])
def register():
    try:
        # pull form submission data.
        # encrypt sensitive information like email and password
        email = request.json["email"].lower()
        password_encrypted = pbkdf2_sha256.encrypt(request.json["password"])
        name = request.json["name"]

        # check to see if user already exists; else, communicate with user that an
        # account already exists
        try:
            new_user = User(name=name, email=email, password=password_encrypted)
            # if this is a new account, save to database
            new_user.save()
        except user_db.NotUniqueError:
            return jsonify({"error": "User with that email already exists"})
        return jsonify({"success": True})
    except:
        # there was an error while processing form submission
        return jsonify({"error": "Invalid form"})
    

if __name__ == "__main__":
    app.run(debug=True) # debug=True restarts the server everytime we make a change in our code