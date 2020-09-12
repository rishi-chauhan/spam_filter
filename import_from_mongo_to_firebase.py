"""send data from mongo to firebase"""
from pymongo import MongoClient
import functions                        # from functions.py

# set up MongoDB
MONGO_CLIENT = MongoClient()
MONGO_DB = MONGO_CLIENT.project
MONGO_COLLECTION = MONGO_DB.spam

FIREBASE_DB = functions.set_up_firebase()       # connect to firebase realtime database

# initialise empty dictionaries to get data from local MongoDB Database and then store the
# respective data in the dictionaries as the data that is to be stored is in key-value pairs
IP = {}                 # to store IPs
USERNAME = {}           # to store usernames
EMAIL = {}              # to store email addresses
WORDS = {}              # to store common spam words

# get data from local MongoDB and store that in respective dictionaries
for i in MONGO_COLLECTION.find():
    for j in i["ip"]:
        # replace . with + because it is not allowed in firebase
        IP[functions.format_data_for_firebase(j)] = 0
    for k in i["email"]:
        # replace . with + because it is not allowed in firebase
        EMAIL[functions.format_data_for_firebase(str(k))] = 0
    for l in i["username"]:
        USERNAME[functions.format_data_for_firebase(l)] = 0

# a dictionary that'll store data that is to be input the firebase
DATA = {"ip": IP, "email": EMAIL, "username": USERNAME}

# sending data to firebase
# firebase_db.set(data)
