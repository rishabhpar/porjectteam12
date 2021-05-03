from unittest.mock import Mock, patch

from nose.tools import assert_is_not_none, assert_list_equal, assert_true, assert_equals
from app_handler import *
from passlib.hash import pbkdf2_sha256

# To test use the following command: nosetests --verbosity=2 --nocapture tests/test_app_handler.py 

# Tests for login_handler 

@patch('app_handler.Account_Info.find_one')
def test_login_handler_happy(mock_find_one):
    email = "test@test.com"
    password = "Hello123!"
    request_data = {"email": email, "password": password}

    # Configure the mock_find_one to return the user with email and password that match the login attempts
    mock_find_one.return_value = {"email": (bcrypt.hashpw(str.encode(email), salt)).decode(), "password": pbkdf2_sha256.hash(password)}

    # Call the handler
    response = login_handler(request_data)
    # If the request is sent successfully, then I expect a success = true response.
    assert_true(response["success"])

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