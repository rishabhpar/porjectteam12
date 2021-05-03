from unittest.mock import Mock, patch

from nose.tools import assert_is_not_none, assert_list_equal, assert_true, assert_equals
from app_handler import *
from passlib.hash import pbkdf2_sha256
import bcrypt
import json
import random
import string
import requests

# To test use the following command: nosetests --verbosity=2 --nocapture tests/test_app_handler.py 

f = open("extra/salt.txt", "r")
salt = f.readline().encode()
f.close()
#################################################################################################################################
# Tests for login_handler 

# test bad email
@patch('app_handler.Account_Info.find_one')
def test_login_handler_bad_email(mock_find_one):
    email = "hubblabubbla@yahoo.com"
    password = "Testing123!"

    request_data = {"email": email, "password": password}

    endpoint = "http://backendteam12.herokuapp.com/api/login"
    response = requests.post(endpoint, json=request_data)

    assert_equals(response.json()["error"], "Entered email is not associated with a user")


#test bad password
@patch('app_handler.Account_Info.find_one')
def test_login_handler_bad_password(mock_find_one):
    request_data = {"email": (bcrypt.hashpw(str.encode("testingme@gmail.com"), salt)).decode(), "password": pbkdf2_sha256.hash("Hi")}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = request_data
    # Call the handler
    response = login_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_equals(response["error"], "Incorrect Password")

#test empty form
@patch('app_handler.Account_Info.find_one')
def test_login_handler_empty_form(mock_find_one):
    email = ""
    password = ""
    request_data = {"email": email, "password": password}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = request_data

    # Call the handler
    response = login_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_equals(response["error"], "Problem with Form")

@patch('app_handler.Account_Info.find_one')
def test_login_handler_happy(mock_find_one):
    f = open("tests/test_password.txt", "r")
    password = f.readline()

    email = "jigglypuff@test.com"
    request_data = {"email": email, "password": password}
    f.close()
    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = {"email": (bcrypt.hashpw(str.encode(email), salt)).decode(), "password": pbkdf2_sha256.hash(password)}

    # Call the handler
    response = login_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_true(response["success"])

#################################################################################################################################
# Tests for register_handler 

# test with existing user
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.insert_one')
def test_register_handler_user_already_exists(mock_find_one, mock_insert_one):
    email = "jigglypuff@test.com"
    password = "Testing123!"
    confirm_password = "Testing123!"
    name = "Rish"
    request_data = {"email": email, "password": password, "confirm_password": confirm_password, "name": name}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = {"email": (bcrypt.hashpw(str.encode(email), salt)).decode()}
    mock_insert_one.return_value = {"email": (bcrypt.hashpw(str.encode(email), salt)).decode(), 
                            "password": pbkdf2_sha256.hash(password), 
                            "confirm_password": pbkdf2_sha256.hash(confirm_password), 
                            "name": name}

    # Call the handler
    response = register_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_equals(response["error"], "User with that email already exists")
    
# test with weak password - too little characters
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.insert_one')
def test_register_handler_weak_password(mock_find_one, mock_insert_one):
    email = "testingme@gmail.com"
    password = "Hi"
    confirm_password = "Hi"
    name = "Rish"
    request_data = {"email": email, "password": password, "confirm_password": confirm_password, "name": name}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = {"email": (bcrypt.hashpw(str.encode(email), salt)).decode()}
    mock_insert_one.return_value = None
    # Call the handler
    response = register_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_true(response["error"], "Password is not strong enough. Minimums: 8 characters, 1 uppercase, 1 number, 1 special")


# test with weak password - no uppercase
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.insert_one')
def test_register_handler_no_uppercase(mock_find_one, mock_insert_one):
    email = "testingme@gmail.com"
    password = "testing123!"
    confirm_password = "testing123!"
    name = "Rish"
    request_data = {"email": email, "password": password, "confirm_password": confirm_password, "name": name}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = {"email": (bcrypt.hashpw(str.encode(email), salt)).decode()}
    mock_insert_one.return_value = None
    # Call the handler
    response = register_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_true(response["error"], "Password is not strong enough. Minimums: 8 characters, 1 uppercase, 1 number, 1 special")


# test with weak password - no numbers
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.insert_one')
def test_register_handler_no_numbers(mock_find_one, mock_insert_one):
    email = "testingme@gmail.com"
    password = "Testing!"
    confirm_password = "Testing!"
    name = "Rish"
    request_data = {"email": email, "password": password, "confirm_password": confirm_password, "name": name}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = {"email": (bcrypt.hashpw(str.encode(email), salt)).decode()}
    mock_insert_one.return_value = None
    # Call the handler
    response = register_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_true(response["error"], "Password is not strong enough. Minimums: 8 characters, 1 uppercase, 1 number, 1 special")


# test with weak password - no special
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.insert_one')
def test_register_handler_no_special(mock_find_one, mock_insert_one):
    email = "testingme@gmail.com"
    password = "Testing123"
    confirm_password = "Testing123"
    name = "Rish"
    request_data = {"email": email, "password": password, "confirm_password": confirm_password, "name": name}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = {"email": (bcrypt.hashpw(str.encode(email), salt)).decode()}
    mock_insert_one.return_value = None
    # Call the handler
    response = register_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_true(response["error"], "Password is not strong enough. Minimums: 8 characters, 1 uppercase, 1 number, 1 special")


# test with mismatched passwords
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.insert_one')
def test_register_handler_mismatched_passwords(mock_find_one, mock_insert_one):
    email = "testingme@gmail.com"
    password = "Testing123!"
    confirm_password = "Testing1!"
    name = "Rish"
    request_data = {"email": email, "password": password, "confirm_password": confirm_password, "name": name}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = {"email": (bcrypt.hashpw(str.encode(email), salt)).decode()}
    mock_insert_one.return_value = None
    # Call the handler
    response = register_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_true(response["error"], "Passwords do not match")


#test empty form
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.insert_one')
def test_register_handler_empty_form(mock_find_one, mock_insert_one):
    email = ""
    password = ""
    request_data = {"email": email, "password": password}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = request_data
    mock_insert_one.return_value = None
    # Call the handler
    response = register_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_equals(response["error"], "Invalid form")


# happy case
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.insert_one')
def test_register_handler_happy_case(mock_find_one, mock_insert_one):
    letters = string.ascii_lowercase
    title = ''.join(random.choice(letters) for i in range(10)) 
    # Send a request to the register endpoint and store the response
    register_credentials = {"email": title + "@testing.com", "password": "Testing123!", "confirm_password":"Testing123!", "name":"Rish"}
    endpoint = "http://backendteam12.herokuapp.com/api/register"
    response = requests.post(endpoint, json=register_credentials)

    assert_true(response.json()["success"])

#################################################################################################################################
# Tests for updatepassword_handler 

# test non existing user
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.update_one')
def test_updatepass_nonexisting_user(mock_find_one, mock_update_one):
    email = "happyhappy@lilducky.com"
    currentPassword = "Testing123!"
    newPassword = "newPass123!"
    accountType = "user"
    request_data = {"email": "happyhappy@lilducky.com", "currentPassword": "Testing123!", "newPassword": "newPass123!", "accountType": "user"}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value ={"email": (bcrypt.hashpw(str.encode(email), salt)).decode()}
    mock_update_one.return_value = None
    # Call the handler
    response = updatepassword_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_equals(response["error"], "Entered email is not associated with a user")

# test incorrect password
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.update_one')
def test_updatepass_handler_incorrect_password(mock_find_one, mock_update_one):
    # Send a request to the updatepassword endpoint and store the response
    password_data = {"email": "jigglypuff@test.com", "currentPassword": "hihihihi", "newPassword": "newpass", "accountType": "user"}
    endpoint = "http://backendteam12.herokuapp.com/api/updatepassword"
    response = requests.post(endpoint, json=password_data)

    assert_equals(response.json()["error"], "Incorrect Password")
    
#test empty form
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.insert_one')
def test_updatepass_handler_empty_form(mock_find_one, mock_update_one):
    request_data = {"email": "", "currentPassword": "", "newPassword": "", "accountType": "user"}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = request_data
    mock_update_one.return_value = None
    # Call the handler
    response = updatepassword_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_equals(response["error"], "Entered email is not associated with a user")


# happy case
@patch('app_handler.Account_Info.find_one')
@patch('app_handler.Account_Info.insert_one')
def test_updatepass_handler_happy_case(mock_find_one, mock_insert_one):
    letters = string.ascii_lowercase
    newpass = ''.join(random.choice(letters) for i in range(10)) 

    f = open("tests/test_password.txt", "r")
    password = f.readline()
    f.close()

    password_data = {"email": "jigglypuff@test.com", "currentPassword": password, "newPassword": newpass, "accountType": "user"}
    
    f = open("tests/test_password.txt", "w")
    f.write(newpass)
    f.close()

    endpoint = "http://backendteam12.herokuapp.com/api/updatepassword"
    response = requests.post(endpoint, json=password_data)

    assert_true(response.json()["success"])

###################################################################################################################################

# Tests for hardware_handler
#check out working
@patch('app_handler.Hardware_Info.update_one')
@patch('app_handler.Hardware_Info.find_one')
def test_hardware_handler_out1_happy(mock_find_one, mock_update_one):
    set1 = "10"
    set2 = "5"
    check1 = "out"
    check2 = "out"
    id = "projectid"

    request_data = {"set1":set1, "set2":set2, "check1": check1, "check2": check2, "id": id}

    used1 = 10
    used2 = 10
    cap1 = 90
    cap2 = 90
    mock_find_one.return_value = {"projectid": id, "used1": used1, "used2": used2, "cap1": cap1, "cap2": cap2}
    mock_update_one.return_value = None

    response = hardware_handler(request_data)
    assert_equals(response["projectid"], id)
    assert_equals(response["used1"], used1 + int(set1))
    assert_equals(response["used2"], used2 + int(set2))
    assert_equals(response["cap1"], cap1 - int(set1))
    assert_equals(response["cap2"], cap2 - int(set2))

#check in working
@patch('app_handler.Hardware_Info.update_one')
@patch('app_handler.Hardware_Info.find_one')
def test_hardware_handler_in1_happy(mock_find_one, mock_update_one):
    set1 = "5"
    set2 = "10"
    check1 = "in"
    check2 = "in"
    id = "projectid"

    request_data = {"set1":set1, "set2":set2, "check1": check1, "check2": check2, "id": id}

    used1 = 10
    used2 = 10
    cap1 = 90
    cap2 = 90
    mock_find_one.return_value = {"projectid": id, "used1": used1, "used2": used2, "cap1": cap1, "cap2": cap2}
    mock_update_one.return_value = None

    response = hardware_handler(request_data)
    assert_equals(response["projectid"], id)
    assert_equals(response["used1"], used1 - int(set1))
    assert_equals(response["used2"], used2 - int(set2))
    assert_equals(response["cap1"], cap1 + int(set1))
    assert_equals(response["cap2"], cap2 + int(set2))    

#set1 check out error (overflow)
@patch('app_handler.Hardware_Info.update_one')
@patch('app_handler.Hardware_Info.find_one')
def test_hardware_handler_out1_error(mock_find_one, mock_update_one):
    set1 = "99"
    set2 = "0"
    check1 = "out"
    check2 = "out"
    id = "projectid"

    request_data = {"set1":set1, "set2":set2, "check1": check1, "check2": check2, "id": id}

    used1 = 10
    used2 = 10
    cap1 = 90
    cap2 = 90
    mock_find_one.return_value = {"projectid": id, "used1": used1, "used2": used2, "cap1": cap1, "cap2": cap2}
    mock_update_one.return_value = None

    response = hardware_handler(request_data)
    assert_equals(response["error"], "Set 1 value invalid")       

#set2 check out error (overflow)
@patch('app_handler.Hardware_Info.update_one')
@patch('app_handler.Hardware_Info.find_one')
def test_hardware_handler_out2_error(mock_find_one, mock_update_one):
    set1 = "0"
    set2 = "99"
    check1 = "out"
    check2 = "out"
    id = "projectid"

    request_data = {"set1":set1, "set2":set2, "check1": check1, "check2": check2, "id": id}

    used1 = 10
    used2 = 10
    cap1 = 90
    cap2 = 90
    mock_find_one.return_value = {"projectid": id, "used1": used1, "used2": used2, "cap1": cap1, "cap2": cap2}
    mock_update_one.return_value = None

    response = hardware_handler(request_data)
    assert_equals(response["error"], "Set 2 value invalid")    

#set1 check in error 
@patch('app_handler.Hardware_Info.update_one')
@patch('app_handler.Hardware_Info.find_one')
def test_hardware_handler_in1_error(mock_find_one, mock_update_one):
    set1 = "15"
    set2 = "0"
    check1 = "in"
    check2 = "in"
    id = "projectid"

    request_data = {"set1":set1, "set2":set2, "check1": check1, "check2": check2, "id": id}

    used1 = 10
    used2 = 10
    cap1 = 90
    cap2 = 90
    mock_find_one.return_value = {"projectid": id, "used1": used1, "used2": used2, "cap1": cap1, "cap2": cap2}
    mock_update_one.return_value = None

    response = hardware_handler(request_data)
    assert_equals(response["error"], "Set 1 value invalid")        

#set2 check in error 
@patch('app_handler.Hardware_Info.update_one')
@patch('app_handler.Hardware_Info.find_one')
def test_hardware_handler_in2_error(mock_find_one, mock_update_one):
    set1 = "0"
    set2 = "20"
    check1 = "in"
    check2 = "in"
    id = "projectid"

    request_data = {"set1":set1, "set2":set2, "check1": check1, "check2": check2, "id": id}

    used1 = 10
    used2 = 10
    cap1 = 90
    cap2 = 90
    mock_find_one.return_value = {"projectid": id, "used1": used1, "used2": used2, "cap1": cap1, "cap2": cap2}
    mock_update_one.return_value = None

    response = hardware_handler(request_data)
    assert_equals(response["error"], "Set 2 value invalid")    

###################################################################################################################            