# package to interface with mongodb
import pymongo
# Needed to verify the server is who it says it is. Mac won't work without and Cloud stuff might not either.
import certifi

client = pymongo.MongoClient("mongodb+srv://team12:adminBois&Gorls@cluster0.82uuk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())
# get the specific database for user information
User_DB = client.get_database('user_information')
Account_Info = User_DB.users

Project_DB = client.get_database('project_information')
Project_Info = Project_DB.projects

Datasets_DB = client.get_database('dataset_information')
Datasets_Info = Datasets_DB.datasets

Hardware_DB = client.get_database('hardware_information')
Hardware_Info = Hardware_DB.hardware