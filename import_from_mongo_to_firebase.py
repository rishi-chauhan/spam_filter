from pymongo import MongoClient
import functions

mongo_client = MongoClient()

mongo_db = mongo_client.project

mongo_collection = mongo_db.spam

fbase = functions.firebase()
firebase_connect = fbase.firebase_config
firebase_db = firebase_connect.database()
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
        username[fbase.formatDataForFirebase(l)] = 0

print username

# for i in username:
#     if "#" in i:
#         print i

# data = {"ip": ip, "email": email, "username": username}
#
# firebase_db.set(data)
