"""
This script helps in updating the database by going through all the spam mails in the account.
"""

import imaplib
import email
import getpass
from pymongo import MongoClient
import functions

# set up MongoDB
MONGO_CLIENT = MongoClient()
MONGO_DB = MONGO_CLIENT.project
MONGO_COLLECTION = MONGO_DB.spam

# making a imap variable to access client's(here Gmail) all services
MAIL = imaplib.IMAP4_SSL("imap.gmail.com")

USERNAME = input("Email ID: ")
PASSWORD = getpass.getpass()

functions.login(MAIL, USERNAME, PASSWORD)

RV, DATA = MAIL.select("[Gmail]/Spam")

if RV == 'OK':
    for num in range(int(DATA[0])):
        rv, data = MAIL.fetch(num+1, '(RFC822)')

        print(num+1, "\n")
        msg = str(email.message_from_string(data[0][1]))

        for w in msg:
            cursor = MONGO_DB.spam.find({})

        if rv != 'OK':
            print("ERROR getting message", num)

MAIL.close()

functions.logout(MAIL)
