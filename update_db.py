################################################################################################
#This script helps in updating the database by going through all the spam mails in the account.#
################################################################################################

# html to text

from pymongo import MongoClient
import get_email_details
import imaplib
import email

# creating a client
client = MongoClient()

# connecting to db
db = client.project

# connecting to collection
collection = db.spam

# making a imap variable to access client's(here Gmail) all services
mail = imaplib.IMAP4_SSL("imap.gmail.com")

try:
    print "Connecting to Gmail....\nLog in....."
    # for testing
    mail.login("rishi.darkknight.chauhan", "hwgrglpigpdlixxr")
    # for general purpose
    # mail.login(username, getpass.getpass())
    print "\nConnected."
except imaplib.IMAP4.error:
    # login Failed
    print "Login Failed!!"
    print "\n1. If you have a 2-way verification for your Gmail account go to \"  https://security.google.com/settings/security/apppasswords\" and create an app password. \n2. Go to  \"https://www.google.com/settings/security/lesssecureapps\" and enable less secure apps permission"

rv, data = mail.select("[Gmail]/Spam")

if rv == 'OK':
    for num in range(int(data[0])):
        rv, data = mail.fetch(num+1, '(RFC822)')

        print num+1, "\n"
        msg = str(email.message_from_string(data[0][1]))

        for w in msg:
            cursor = db.spam.find({})
            # if
            #     print "yes"

        if rv != 'OK':
            print "ERROR getting message", num

mail.close()

print "\nLoging out..."
mail.logout()
print "Log out successful.\nHave a good day! :)"
