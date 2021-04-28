from unittest import mock
from nose.tools import assert_true
import requests
import json

# To test use the following command: nosetests --verbosity=2 --nocapture test_app_endpoints.py 
# The --nocapture flag allows for the print statements to show up

#This is to test that the login endpoint is up and returns an ok response
def test_login_endpoint():
    # Send a request to the login endpoint and store the response
    login_credentials = {"email":"am@gmail.com","password":"Hello123!"}
    endpoint = "http://backendteam12.herokuapp.com/api/login"
    response = requests.post(endpoint, json=login_credentials)

    print(response.json())

    assert_true(response.ok)

# This is to test that the register endpoint is up and returns an ok response
def test_register_endpoint():
    # Send a request to the register endpoint and store the response
    register_credentials = {"name":"name","email":"a@gmail.com","password":"Hello123!","confirm_password":"Hello123!"}
    endpoint = "http://backendteam12.herokuapp.com/api/register"
    response = requests.post(endpoint, json=register_credentials)

    print(response.json())

    assert_true(response.ok)

# This is to test that the newproject endpoint is up and returns an ok response
def test_newproject_endpoint():
    # Send a request to the newproject endpoint and store the response
    project_data = {"projectid": "PabloEscobar", "projName":"name", "description":"desc", "password":"Project1"}
    endpoint = "http://backendteam12.herokuapp.com/api/newproject"
    response = requests.post(endpoint, json=project_data)

    print(response.json())

    assert_true(response.ok)

# This is to test that the dashboard endpoint is up and returns an ok response
def test_dashboard_endpoint():
    # Send a request to the dashboard endpoint and store the response
    project_login = {"searchid": "PabloEscobar", "password":"Project1"}
    endpoint = "http://backendteam12.herokuapp.com/api/dashboard"
    response = requests.post(endpoint, json=project_login)

    print(response.json())

    assert_true(response.ok)

# This is to test that the hardware endpoint is up and returns an ok response
def test_hardware_endpoint():
    # Send a request to the hardware endpoint and store the response
    hardware_changes = {"set1": 10, "set2":10, "check1":"out", "check2":"out", "id":"PabloEscobar"}
    endpoint = "http://backendteam12.herokuapp.com/api/hardware"
    response = requests.post(endpoint, json=hardware_changes)

    print(response.json())

    assert_true(response.ok)

# This is to test that the deleteproject endpoint is up and returns an ok response
def test_deleteproject_endpoint():
    # Send a request to the deleteproject endpoint and store the response
    delete_project = {"projectid": "PabloEscobar", "password":"Project1"}
    endpoint = "http://backendteam12.herokuapp.com/api/deleteproject"
    response = requests.post(endpoint, json=delete_project)

    print(response.json())

    assert_true(response.ok)

# This is to test that the projectdetails endpoint is up and returns an ok response
def test_projectdetails_endpoint():
    # Send a request to the projectdetails endpoint and store the response
    project_data = {"projectid": "PabloEscobar", "password":"Project1"}
    endpoint = "http://backendteam12.herokuapp.com/api/projectdetails"
    response = requests.post(endpoint, json=project_data)

    print(response.json())

    assert_true(response.ok)

# This is to test that the updatepassword endpoint is up and returns an ok response
def test_updatepassword_endpoint():
    # Send a request to the updatepassword endpoint and store the response
    password_data = {"currentPassword": "Hello123!", "newPassword":"Bye123!!", "accountType":"user", "email":"a@gmail.com"}
    endpoint = "http://backendteam12.herokuapp.com/api/updatepassword"
    response = requests.post(endpoint, json=password_data)

    print(response.json())

    assert_true(response.ok)

# This is to test that the getdatasets endpoint is up and returns an ok response
def test_getdatasets_endpoint():
    # Send a request to the getdatasets endpoint and store the response
    endpoint = "http://backendteam12.herokuapp.com/api/getdatasets"
    response = requests.get(endpoint)

    print(response.json())

    assert_true(response.ok)