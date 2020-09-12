"""
This script is the main script that executes and shows the result.
"""
import imaplib
import getpass
from sklearn import tree
from pymongo import MongoClient
import functions

MAIL = imaplib.IMAP4_SSL("imap.gmail.com")
USERNAME = input("Email ID: ")
PASSWORD = getpass.getpass()

functions.login(MAIL, USERNAME, PASSWORD)

CLIENT = MongoClient()

# connecting to database
DB = CLIENT.train

IP, SENDER = functions.get_details(MAIL, "INBOX")

EMAIL_IP = IP
EMAIL_USERNAME = SENDER[0]
EMAIL_EMAIL = SENDER[1]

IP_CHECK = 0
EMAIL = 0
USERNAME = 0
WORDS = 0

# selecting collection
COLLECTION = DB.train_c

RESULT = DB.train_c.find({"$or": [{"ip": EMAIL_IP}, {"username": EMAIL_USERNAME},
                                  {"email": EMAIL_EMAIL}]})
for i in RESULT:
    if EMAIL_IP in i["ip"]:
        IP_CHECK = 1
    if EMAIL_USERNAME in i["username"]:
        USERNAME = 1
    if EMAIL_EMAIL in i["email"]:
        EMAIL = 1

# [ip, username, email, words]
FEATURES = [[0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1]]
# spam = 1, not spam = 0
LABELS = [0, 1, 1, 1, 1, 1]

print("\nIP: ", EMAIL_IP, "\nUsername: ", EMAIL_USERNAME, "\nE-mail ID: ", EMAIL_EMAIL)
# print ip_check, username, email

CLF = tree.DecisionTreeClassifier()
CLF = CLF.fit(FEATURES, LABELS)
TEST = [[IP_CHECK, USERNAME, EMAIL, WORDS]]

if CLF.predict(TEST)[0] == 1:
    print("\nSpam")
else:
    print("\nNot Spam")

functions.logout(MAIL)
