import json
import requests
import os.path
from os import path

# test the register function
if not path.exists('log/register_log.txt'):
    register = open("cases/register.txt", "r")
    reg_log = open("log/register_log.txt", "w")

    url = 'http://127.0.0.1:5000/api/register'
    headers = {'content-type': 'application/json'}

    line = register.readline()

    while line != "":
        print(line)
        reg_log.write(line + '\n')

        payload = json.loads(register.readline())

        r = requests.post(url, json=payload, headers=headers)
        reg_log.write(str(r.json()) + "\n\n\n")
        
        line = register.readline()

    register.close()
    reg_log.close()


# test the login function
if not path.exists('log/login_log.txt'):
    login = open("cases/login.txt", "r")
    login_log = open("log/login_log.txt", "w")

    url = 'http://127.0.0.1:5000/api/login'
    headers = {'content-type': 'application/json'}

    line = login.readline()

    while line != "":
        print(line)
        login_log.write(line + '\n')

        payload = json.loads(login.readline())

        r = requests.post(url, json=payload, headers=headers)
        login_log.write(str(r.json()) + "\n\n\n")
        
        line = login.readline()

    login.close()
    login_log.close()


# test the update user password function
if not path.exists('log/updateuserpassword_log.txt'):
    updateuserpass = open("cases/updatepassword.txt", "r")
    updateuserpass_log = open("log/updateuserpassword_log.txt", "w")

    url = 'http://127.0.0.1:5000/api/updatepassword'
    headers = {'content-type': 'application/json'}

    line = updateuserpass.readline()

    while line != "":
        print(line)
        updateuserpass_log.write(line + '\n')

        payload = json.loads(updateuserpass.readline())

        r = requests.post(url, json=payload, headers=headers)
        updateuserpass_log.write(str(r.json()) + "\n\n\n")
        
        line = updateuserpass.readline()

    updateuserpass.close()
    updateuserpass_log.close()