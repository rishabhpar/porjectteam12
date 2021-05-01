from flask import Flask, request, jsonify
# cors is used to relax security, only for development
from flask_cors import CORS
# use bcrypt to hash the email such that the same string hash the same hash
import bcrypt
# import api handler functions
from app_handler import *

# create a Flask app
app = Flask(__name__)
CORS(app)

# A simple home page to backend server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route("/api/login", methods=["POST"])
def login():
    """
    API to login

    Parameters
    ----------
    email : string
    password : string

    Returns
    -------
    json
        with keys "success" or "error"
    """
    return login_handler(request.json)

@app.route("/api/register", methods=["POST"])
def register():
    """
    API to register

    Parameters
    ----------
    email : string
    password : string
    confirm_password : string
    name : string

    Returns
    -------
    json
        with keys "success" or "error"
    """
    return register_handler(request.json)
    
@app.route("/api/newproject", methods=["POST"])
def newproject():
    """
    API to create a newproject

    Parameters
    ----------
    projectid : string
    password : string
    projName : string
    description : string

    Returns
    -------
    json
        with keys "success" or "error"
    """
    return newproject_handler(request.json)     

@app.route("/api/dashboard", methods=["POST"])
def dashboard():
    """
    API to login to hardware dashboard

    Parameters
    ----------
    searchid : string
    password : string

    Returns
    -------
    json
        with keys "success" or "error"
    """
    return dashboard_handler(request.json)
     
@app.route("/api/hardware", methods=["POST"])
def hardware():
    """
    API to check in and checkout hardware resources

    Parameters
    ----------
    set1 : string
    set2 : string
    check1 : string
    check2 : string
    id : string

    Returns
    -------
    json
        with keys "success" or "error"
    """
    return hardware_handler(request.json)

@app.route("/api/deleteproject", methods=["POST"])
def deleteproject():
    """
    API to delete a project

    Parameters
    ----------
    projectid : string
    password : string

    Returns
    -------
    json
        with keys "success" or "error"
    """
    return deleteproject_handler(request.json)

@app.route("/api/projectdetails", methods=["POST"])
def projectdetails():
    """
    API to see project details

    Parameters
    ----------
    projectid : string

    Returns
    -------
    json
        with keys "details" or "error"
    """
   return projectdetails_handler(request.json)

@app.route("/api/updatepassword", methods=["POST"])
def updatepassword():
    """
    API to updatepassword

    Parameters
    ----------
    currentPassword : string
    newPassword : string
    accountType : string
    projectid : string
    email : string

    Returns
    -------
    json
        with keys "success" or "error"
    """
    return updatepassword_handler(request.json)

@app.route("/api/getdatasets", methods=["GET"])
def getdatasets():
    """
    API to getDatasets

    Returns
    -------
    json
        with keys "datasets" or "error"
    """
    return getdatasets_handler()

if __name__ == "__main__":
    app.run(debug=True) # debug=True restarts the server everytime we make a change in our code