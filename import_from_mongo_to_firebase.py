import functions                        # from functions.py
from pymongo import MongoClient

# set up MongoDB
mongo_client = MongoClient()
mongo_db = mongo_client.project
mongo_collection = mongo_db.spam

firebase_db = functions.setUpFirebase()       # connect to firebase realtime database

# initialise empty dictionaries to get data from local MongoDB Database and then store the respective data in the dictionaries as the data that is to be stored is in key-value pairs
ip = {}                 # to store IPs
username = {}           # to store usernames
email = {}              # to store email addresses
words = {}              # to store common spam words

# get data from local MongoDB and store that in respective dictionaries
for i in mongo_collection.find():
    for j in i["ip"]:
        # replace . with + because it is not allowed in firebase
        ip[functions.formatDataForFirebase(j)] = 0
    for k in i["email"]:
        # replace . with + because it is not allowed in firebase
        email[functions.formatDataForFirebase(str(k))] = 0
    for l in i["username"]:
        username[functions.formatDataForFirebase(l)] = 0

# a dictionary that'll store data that is to be input the firebase
data = {"ip": ip, "email": email, "username": username}

# sending data to firebase
# firebase_db.set(data)
