from unittest import mock
from nose.tools import assert_true
import requests
import json

# To test use the following command: nosetests --verbosity=2 --nocapture test_app.py 
# The --nocapture flag allows for the print statements to show up

#This is to test that the login endpoint is up and returns an ok response
def test_login_endpoint():
    # Send a request to the login endpoint and store the response
    login_credentials = {"email":"am@gmail.com","password":"Hello123!"}
    endpoint = "http://backendteam12.herokuapp.com/api/login"
    response = requests.post(endpoint, json = login_credentials)

    print(response.json())

    assert_true(response.ok)

# This is to test that the newproject endpoint is up and returns an ok response
def test_newproject_endpoint():
    # Send a request to the newproject endpoint and store the response
    project_data = {"projectid": "PabloEscobar", "projName":"name", "description":"desc", "password":"Project1"}
    endpoint = "http://backendteam12.herokuapp.com/api/newproject"
    response = requests.post(endpoint, json = project_data)

    print(response.json())

    assert_true(response.ok)

# This is to test that the register endpoint is up and returns an ok response
def test_register_endpoint():
    # Send a request to the register endpoint and store the response
    register_credentials = {"name":"name","email":"a@gmail.com","password":"Hello123!","confirm_password":"Hello123!"}
    endpoint = "http://backendteam12.herokuapp.com/api/register"
    response = requests.post(endpoint, json = register_credentials)

    print(response.json())

    assert_true(response.ok)