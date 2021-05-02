# use bcrypt to hash the email such that the same string hash the same hash
import bcrypt
#Used to have proper log statements until error handling is fully implented
import sys
# passlib is the package we will use to encrypt passwords
from passlib.hash import pbkdf2_sha256
# get access to mongodb tables
from db import Account_Info, Project_Info, Datasets_Info, Hardware_Info
# import password_strength to ensure the user's password is strong
from password_strength import PasswordPolicy

# create a password policy to ensure strong passwords from users
policy = PasswordPolicy.from_names(
    length=8,  # min length: 8
    uppercase=1,  # need min. 1 uppercase letters
    numbers=1,  # need min. 1 digits
    special=1,  # need min. 1 special characters
)

# the seed for hashing a string using bcrypt
# should probably hide this
f = open("extra/salt.txt", "r")
salt = f.readline().encode()
f.close()


#handles the login endpoint's business logic
def login_handler(request_data):  
    try:
        # extract information from the submission form
        email = request_data["email"]
        email_hashed = (bcrypt.hashpw(str.encode(email), salt)).decode()
        password = request_data["password"]

        # check for an existing user's email in the database using the way
        # the email is stored in the database
        user = Account_Info.find_one({"email": email_hashed})

        # if a user exists and the password entered in the form
        # matches, this is a successful login; else, it is an error
        # so we send back feedback
        if user and pbkdf2_sha256.verify(password, user['password']):
            return {"success": True}
        else:
            if user is None:
                # if a user with entered email does not exist, send a feedback message
                return {"error": "Entered email is not associated with a user"}
            return {"error": "Incorrect Password"}
    except:
        return {"error": "Problem with Form"}


#handles the register endpoint's business logic
def register_handler(request_data):
    try:
        # pull form submission data.
        # encrypt sensitive information like email and password
        email = request_data["email"].lower()
        email_hashed = bcrypt.hashpw(str.encode(email), salt).decode()
        password = request_data["password"]
        confirm_password = request_data["confirm_password"]
        name = request_data["name"]

        # confirm the password the user chooses is strong
        if len(policy.test(password)) > 0:
            return {"error": "Password is not strong enough. Minimums: 8 characters, 1 uppercase, 1 number, 1 special"}

        # make sure the user confirms the password properly
        if password != confirm_password:
            return {"error": "Passwords do not match"}
        
        # check to see if user already exists; else, communicate with user that an
        # account already exists
        if Account_Info.find_one({"email": email_hashed}) is not None:
            return {"error": "User with that email already exists"}
        else:
            Account_Info.insert_one({"name":name, "email":email_hashed, "password":pbkdf2_sha256.hash(password)})
            
        return {"success": True}
    except:
        # there was an error while processing form submission
        return {"error": "Invalid form"}


#handles the newproject endpoint's business logic
def newproject_handler(request_data):
    try:
        # pull form submission data.
        # encrypt sensitive information like project id
        projectID = request_data["projectid"]
        projpassword = request_data["password"]
        projectname = request_data["projName"]
        desc = request_data["description"]
        cap = 100
        used = 0
        # confirm the password the user chooses is strong
        #if len(policy.test(projpassword)) > 0:
         #   return jsonify({"error": "Password is not strong enough. Minimums: 8 characters, 1 uppercase, 1 number, 1 special"})
        
        # check to see if project already exists; else, communicate with user that this already exists
        if Project_Info.find_one({"projectid": projectID}) is not None:
            return {"error": "Project with that ID already exists"}
        else:
            Project_Info.insert_one({"projName":projectname, "projectid":projectID,"password":pbkdf2_sha256.hash(projpassword), "description":desc})
            Hardware_Info.insert_one({"projectid":projectID, "cap1": cap, "cap2": cap, "used1": used, "used2":used})
            
        return {"success": True}
    except:
        # there was an error while processing form submission
        return {"error": "Invalid form"}


#handles the dashboard endpoint's business logic
def dashboard_handler(request_data):
    try:
        # pull form submission data.
        # encrypt sensitive information like project id
        searchid = request_data["searchid"]
        password = request_data["password"]
        
        # check to see if project already exists; else, communicate with user that this already exists
        proj = Project_Info.find_one({"projectid": searchid})

        # if a project exists and the password entered in the form
        # matches, this is a successful project
        if proj and pbkdf2_sha256.verify(password, proj['password']):
            return {"success": True}
        else:
            if proj is None:
                return {"error": "Project with that ID does not exist"}
            return {"error": "Incorrect Password"}
    except:
        # there was an error while processing form submission
        return {"error": "Invalid form"}


#handles the hardware endpoint's business logic
def hardware_handler(request_data):
    try:
        #Get the set info from the request 
        set1val = request_data["set1"]
        set2val = request_data["set2"]
        check1 = request_data["check1"].lower()
        check2 = request_data["check2"].lower()
        id = request_data["id"]

        if Hardware_Info.find_one({"projectid": id}) is not None:
            result = Hardware_Info.find_one({"projectid": id})
            used1 = result.get("used1")
            cap1 = result.get("cap1")
            used2 = result.get("used2")
            cap2 = result.get("cap2")

            if check1 == "out":                
                used1 = result.get("used1") + int(set1val)   
                cap1 = result.get("cap1") - int(set1val) 

            if check1 == "in":
                used1 = result.get("used1") - int(set1val) 
                cap1 = result.get("cap1") + int(set1val) 

            if check2 == "out":                
                used2 = result.get("used2") + int(set2val)   
                cap2 = result.get("cap2") - int(set2val) 

            if check2 == "in":
                used2 = result.get("used2") - int(set2val) 
                cap2 = result.get("cap2") + int(set2val)     

            if cap1 > 100 or cap1 < 0:
                return {"error": "Set 1 value invalid"}
            if cap2 > 100 or cap2 < 0:
                return {"error": "Set 2 value invalid"}
        
            Hardware_Info.update_one({"projectid": id}, {"$set": { "used1": int(used1), "used2": int(used2), "cap1": int(cap1), "cap2": int(cap2)}})
            return {"projectid": id, "used1": int(used1), "used2": int(used2), "cap1": int(cap1), "cap2": int(cap2)}
        else:
        #  if a project with projectID does not exist, send a feedback message
            return {"error": "Project does not Exist"}
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return {"error": "Problem with Form"}


#handles the deleteproject endpoint's business logic
def deleteproject_handler(request_data):
    try:
        #Get the projectID from the request (the form might only ask for password)
        #encrypt the projectid to match encryptions in db
        projectID = request_data["projectid"]
        projpassword = request_data["password"]

        #Get the project
        project = Project_Info.find_one({"projectid": projectID})

        if project and pbkdf2_sha256.verify(projpassword, project['password']):
            Project_Info.delete_one({"projectid": projectID})
            return {"success": True}
        else:
            if project is None:
                # if a project with projectID does not exist, send a feedback message
                return {"error": "Project does not Exist"}
            return {"error": "Incorrect Password"}
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return {"error": "Problem with Form"}


#handles the projectdetails endpoint's business logic
def projectdetails_handler(request_data):
    try:
        projectID = request_data["projectid"]
        # Get the project from the projectid
        project = Project_Info.find_one({"projectid": projectID})
        # Handle case of invalid projectid
        if project is None:
            return {"error": "Project with this ID does not exist"}
        # Remove password and db id from response before sending to front end.
        project.pop('_id')
        project.pop('password')
        return {"details" : project}
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return {"error": "Problem with Form"}


#handles the updatepassword endpoint's business logic
def updatepassword_handler(request_data):
    try:
        currentPassword = request_data["currentPassword"]
        newPassword = request_data["newPassword"]

        # This should be either "project" or "user"
        accountType = request_data["accountType"]

        #Handle ProjectCase
        if accountType == "project":
            projectID = request_data["projectid"]
            project = Project_Info.find_one({"projectid": projectID})
            # Verify project exists and that the current password matches
            if project and pbkdf2_sha256.verify(currentPassword, project['password']):
                # Update the password
                Project_Info.update_one({ "projectid": projectID}, { "$set": { "password": pbkdf2_sha256.hash(newPassword)} })
                return {"success": True}
            else:
                # If a project with entered projectid does not exist, send a feedback message
                if project is None:
                    return {"error": "Entered projectID is not associated with a project"}
                return {"error": "Incorrect Password"}

        #Handle User case
        elif accountType == "user":
            email = request_data["email"]
            email_hashed = (bcrypt.hashpw(str.encode(email), salt)).decode()
            user = Account_Info.find_one({"email": email_hashed})
            # Verify user account exists and that the current password matches
            if user and pbkdf2_sha256.verify(currentPassword, user['password']):
                # Update the password
                Account_Info.update_one({ "email": email_hashed}, { "$set": { "password": pbkdf2_sha256.hash(newPassword)} })
                return {"success": True}
            else:
                # If a user with entered email does not exist, send a feedback message
                if user is None:
                    return {"error": "Entered email is not associated with a user"}
                return {"error": "Incorrect Password"}

        else:
            return {"error": "Invalid Account Type"}

    except:
        print("Unexpected error:", sys.exc_info()[0])
        return {"error": "Problem with Form"}


#handles the getdatasets endpoint's business logic
def getdatasets_handler():
    try:
        datasets = Datasets_Info.find({}, { "name": 1, "link": 1, "_id": 0, "description": 1}).limit(10)
        return {"datasets": datasets}
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return {"error": "Problem with Form"}
