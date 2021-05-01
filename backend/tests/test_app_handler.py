from unittest.mock import Mock, patch

from nose.tools import assert_is_not_none, assert_list_equal, assert_true

from app_handler import *
from passlib.hash import pbkdf2_sha256

# import os
# os.chdir("../")
# print("****************************", os.getcwd())

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