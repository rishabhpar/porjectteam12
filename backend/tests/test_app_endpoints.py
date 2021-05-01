from unittest import mock
from nose.tools import assert_true
import requests
import json
import random
import string

# To test use the following command: nosetests --verbosity=2 --nocapture test_app_endpoints.py 
# The --nocapture flag allows for the print statements to show up

#These are 4 tests that the login endpoint is up and returns an ok response
def test_login_endpoint_bad_email():
    # Send a request to the login endpoint and store the response
    login_credentials = {"email": "happyhappy@lilducky.com", "password": "Testing123!"}
    endpoint = "http://backendteam12.herokuapp.com/api/login"
    response = requests.post(endpoint, json=login_credentials)

    assert response.json()["error"] == "Entered email is not associated with a user"


def test_login_endpoint_bad_password():
    # Send a request to the login endpoint and store the response
    login_credentials = {"email": "testingme@gmail.com", "password": "Hi"}
    endpoint = "http://backendteam12.herokuapp.com/api/login"
    response = requests.post(endpoint, json=login_credentials)

    assert response.json()["error"] == "Incorrect Password"


def test_login_endpoint_empty_form():
    # Send a request to the login endpoint and store the response
    login_credentials = {"email": "", "password": ""}
    endpoint = "http://backendteam12.herokuapp.com/api/login"
    response = requests.post(endpoint, json=login_credentials)

    assert response.json()["error"] == "Entered email is not associated with a user"


def test_login_endpoint_happy_case():
    # Send a request to the login endpoint and store the response
    f = open("test_password.txt", "r")
    password = f.readline()

    login_credentials = {"email": "jigglypuff@test.com", "password": password}
    f.close()
    endpoint = "http://backendteam12.herokuapp.com/api/login"
    response = requests.post(endpoint, json=login_credentials)


    assert response.json()["success"] == True

###################################################################################################################################

# These 8 tests that the register endpoint is up and returns an ok response
def test_register_endpoint_user_already_exists():
    # Send a request to the register endpoint and store the response
    register_credentials = {"email": "rishabh.parekh@utexas.edu", "password": "Testing123!", "confirm_password":"Testing123!", "name":"Rish"}
    endpoint = "http://backendteam12.herokuapp.com/api/register"
    response = requests.post(endpoint, json=register_credentials)

    assert response.json()["error"] == "User with that email already exists"

def test_register_endpoint_weak_password_characters():
    # Send a request to the register endpoint and store the response
    register_credentials = {"email": "testingme@gmail.com", "password": "Hi", "confirm_password":"Hi", "name":"Rish"}
    endpoint = "http://backendteam12.herokuapp.com/api/register"
    response = requests.post(endpoint, json=register_credentials)

    assert response.json()["error"] == "Password is not strong enough. Minimums: 8 characters, 1 uppercase, 1 number, 1 special"


def test_register_endpoint_weak_password_uppercase():
    # Send a request to the register endpoint and store the response
    register_credentials = {"email": "testingme@gmail.com", "password": "testing123!", "confirm_password":"testing123!", "name":"Rish"}
    endpoint = "http://backendteam12.herokuapp.com/api/register"
    response = requests.post(endpoint, json=register_credentials)

    assert response.json()["error"] == "Password is not strong enough. Minimums: 8 characters, 1 uppercase, 1 number, 1 special"


def test_register_endpoint_weak_password_numbers():
    # Send a request to the register endpoint and store the response
    register_credentials = {"email": "testingme@gmail.com", "password": "Testing!", "confirm_password":"Testing!", "name":"Rish"}
    endpoint = "http://backendteam12.herokuapp.com/api/register"
    response = requests.post(endpoint, json=register_credentials)

    assert response.json()["error"] == "Password is not strong enough. Minimums: 8 characters, 1 uppercase, 1 number, 1 special"


def test_register_endpoint_weak_password_specials():
    # Send a request to the register endpoint and store the response
    register_credentials = {"email": "testingme@gmail.com", "password": "Testing123", "confirm_password":"Testing123", "name":"Rish"}
    endpoint = "http://backendteam12.herokuapp.com/api/register"
    response = requests.post(endpoint, json=register_credentials)

    assert response.json()["error"] == "Password is not strong enough. Minimums: 8 characters, 1 uppercase, 1 number, 1 special"


def test_register_endpoint_mismatched_passwords():
    # Send a request to the register endpoint and store the response
    register_credentials = {"email": "testingme@gmail.com", "password": "Testing123!", "confirm_password":"Testing1!", "name":"Rish"}
    endpoint = "http://backendteam12.herokuapp.com/api/register"
    response = requests.post(endpoint, json=register_credentials)

    assert response.json()["error"] == "Passwords do not match"


def test_register_endpoint_empty_form():
    # Send a request to the register endpoint and store the response
    register_credentials = {"email": "", "password": "", "confirm_password":"", "name":""}
    endpoint = "http://backendteam12.herokuapp.com/api/register"
    response = requests.post(endpoint, json=register_credentials)

    assert response.json()["error"] == "Password is not strong enough. Minimums: 8 characters, 1 uppercase, 1 number, 1 special"


def test_register_endpoint_happy_case():
    # printing lowercase
    letters = string.ascii_lowercase
    title = ''.join(random.choice(letters) for i in range(10)) 
    # Send a request to the register endpoint and store the response
    register_credentials = {"email": title + "@testing.com", "password": "Testing123!", "confirm_password":"Testing123!", "name":"Rish"}
    endpoint = "http://backendteam12.herokuapp.com/api/register"
    response = requests.post(endpoint, json=register_credentials)

    assert response.json()["success"] == True

###################################################################################################################################

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

###############################################################################################################################

# This is to test that the updatepassword endpoint is up and returns an ok response
def test_updatepassword_endpoint_nonexisting_user():
    # Send a request to the updatepassword endpoint and store the response
    password_data = {"email": "happyhappy@lilducky.com", "currentPassword": "Testing123!", "newPassword": "newPass123!", "accountType": "user"}
    endpoint = "http://backendteam12.herokuapp.com/api/updatepassword"
    response = requests.post(endpoint, json=password_data)

    assert response.json()["error"] == "Entered email is not associated with a user"


def test_updatepassword_endpoint_incorrect_password():
    # Send a request to the updatepassword endpoint and store the response
    password_data = {"email": "jigglypuff@test.com", "currentPassword": "hihihihi", "newPassword": "newpass", "accountType": "user"}
    endpoint = "http://backendteam12.herokuapp.com/api/updatepassword"
    response = requests.post(endpoint, json=password_data)

    assert response.json()["error"] == "Incorrect Password"


def test_updatepassword_endpoint_empty_form():
    # Send a request to the updatepassword endpoint and store the response
    password_data = {"email": "", "currentPassword": "", "newPassword": "", "accountType": "user"}
    endpoint = "http://backendteam12.herokuapp.com/api/updatepassword"
    response = requests.post(endpoint, json=password_data)

    assert response.json()["error"] == "Entered email is not associated with a user"


def test_updatepassword_endpoint_happy_case():
    # Send a request to the updatepassword endpoint and store the response
    letters = string.ascii_lowercase
    newpass = ''.join(random.choice(letters) for i in range(10))

    f = open("test_password.txt", "r")
    password = f.readline()
    f.close()

    password_data = {"email": "jigglypuff@test.com", "currentPassword": password, "newPassword": newpass, "accountType": "user"}
    
    f = open("test_password.txt", "w")
    f.write(newpass)
    f.close()

    endpoint = "http://backendteam12.herokuapp.com/api/updatepassword"
    response = requests.post(endpoint, json=password_data)

    assert response.json()["success"] == True

####################################################################################################################################

# This is to test that the getdatasets endpoint is up and returns an ok response
def test_getdatasets_endpoint():
    # Send a request to the getdatasets endpoint and store the response
    endpoint = "http://backendteam12.herokuapp.com/api/getdatasets"
    response = requests.get(endpoint)

    print(response.json())

    assert_true(response.ok)

####################################################################################################################################
    
#These are 4 tests that the dashboard endpoint is up and returns an ok response for projects
def test_dashboard_endpoint_bad_id():
    # Send a request to the dashboard endpoint and store the response
    id_credentials = {"projectid":"0000", "password": "Testing123!"}
    endpoint = "http://backendteam12.herokuapp.com/api/dashboard"
    response = requests.post(endpoint, json=id_credentials)

    assert response.json()["error"] == "Project with that ID does not exist"


def test_dashboard_endpoint_bad_password():
    # Send a request to the dashboard endpoint and store the response
    id_credentials = {"projectid":"0000", "password": "Testing123!"}
    endpoint = "http://backendteam12.herokuapp.com/api/dashboard"
    response = requests.post(endpoint, json=id_credentials)

    assert response.json()["error"] == "Incorrect Password"


def test_login_endpoint_empty_form():
    # Send a request to the login endpoint and store the response
    id_credentials = {"projectid":" ", "password": " "}
    endpoint = "http://backendteam12.herokuapp.com/api/dashboard"
    response = requests.post(endpoint, json=id_credentials)

    assert response.json()["error"] == "Project with that ID does not exist"


def test_login_endpoint_happy_case():
    # Send a request to the login endpoint and store the response
    id_credentials = {"projectid":"9999", "password": "hello"}
    endpoint = "http://backendteam12.herokuapp.com/api/dashboard"
    response = requests.post(endpoint, json=id_credentials)
    assert response.json()["success"] == True