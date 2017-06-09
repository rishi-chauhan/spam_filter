####################################################################
#This script is the main script that executes and shows the result.#
####################################################################

from sklearn import tree
from pymongo import MongoClient
from functions import emails

emails.login()

client = MongoClient()

# connecting to database
db = client.train

ip, sender = emails.get_details("INBOX")

email_ip = ip
email_username = sender[0]
email_email = sender[1]

ip_check = 0
email = 0
username = 0
words = 0

# selecting collection
collection = db.train_c

result = db.train_c.find({"$or": [{"ip": email_ip}, {"username": email_username}, {"email": email_email}]})
for i in result:
    if email_ip in i["ip"]:
        ip_check = 1
    if email_username in i["username"]:
        username = 1
    if email_email in i["email"]:
        email = 1

# [ip, username, email, words]
features = [[0,0,0,0], [0,1,1,1], [1,1,1,0], [1,0,0,0], [0,0,0,1], [1,1,1,1]]
# spam = 1, not spam = 0
labels = [0,1,1,1,1,1]

print "\nIP: ", email_ip, "\nUsername: ", email_username, "\nE-mail ID: ", email_email
# print ip_check, username, email

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
test = [[ip_check, username, email, words]]

if clf.predict(test)[0] == 1:
    print "\nSpam"
else:
    print "\nNot Spam"

emails.logout()
