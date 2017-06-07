import pyrebase         # for firebase
from pymongo import MongoClient

# config firebase for app
config = {
    "apiKey": "AIzaSyD6oXg-aMBIZ_rK6aSW9uZZcI4ITk_zZJM",
    "authDomain": "spam-filter-e2306.firebaseapp.com",
    "databaseURL": "https://spam-filter-e2306.firebaseio.com",
    "projectId": "spam-filter-e2306",
    "storageBucket": "spam-filter-e2306.appspot.com",
    "messagingSenderId": "438892013228"
  }

mongo_client = MongoClient()

mongo_db = mongo_client.project

mongo_collection = mongo_db.spam

# initialise firebase connection
firebase = pyrebase.initialize_app(config)

# connect to database
firebase_db = firebase.database()

ip = {}
username = {}
email = {}
words = {}

for i in mongo_collection.find():
    for j in i["ip"]:
        # replace . with + because it is not allowed in firebase
        ip[str(j).replace(".", "dot+")] = 0
    for k in i["email"]:
        # replace . with + because it is not allowed in firebase
        email[str(k).replace(".", "dot+")] = 0
    for l in i["username"]:
        l = l.replace(".", "dot+")
        l = l.replace("/", "slash+")
        l = l.replace("#", "slash+")
        username[l] = 0

# for i in username:
#     if "#" in i:
#         print i

data = {"ip": ip, "email": email, "username": username}

firebase_db.set(data)
