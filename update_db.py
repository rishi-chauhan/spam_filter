################################################################################################
#This script helps in updating the database by going through all the spam mails in the account.#
################################################################################################

from pymongo import MongoClient
import imaplib
import email
import functions
import getpass

# set up MongoDB
mongo_client = MongoClient()
mongo_db = mongo_client.project
mongo_collection = mongo_db.spam

# making a imap variable to access client's(here Gmail) all services
mail = imaplib.IMAP4_SSL("imap.gmail.com")

username = raw_input("Email ID: ")
password = getpass.getpass()

functions.logIn(mail, username, password)

rv, data = mail.select("[Gmail]/Spam")

if rv == 'OK':
    for num in range(int(data[0])):
        rv, data = mail.fetch(num+1, '(RFC822)')

        print num+1, "\n"
        msg = str(email.message_from_string(data[0][1]))

        for w in msg:
            cursor = mongo_db.spam.find({})

        if rv != 'OK':
            print "ERROR getting message", num

mail.close()

functions.logOut(mail)
