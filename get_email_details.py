############################################################################################
#This script helps in connecting to the user's email account and retreiving the latest email.#
############################################################################################

import imaplib
import getpass
import email

# making a imap variable to access client's(here Gmail) all services
mail = imaplib.IMAP4_SSL("imap.gmail.com")



# login
def login():
    try:
        print "Connecting to Gmail....\nLogging in....."
        # for testing
        mail.login("rishi.darkknight.chauhan", "hwgrglpigpdlixxr")
        # for general purpose
        # mail.login(username, getpass.getpass())
        print "\nConnected."
    except imaplib.IMAP4.error:
        # login Failed
        print "Login Failed!!"
        print "\n1. If you have a 2-way verification for your Gmail account go to \"  https://security.google.com/settings/security/apppasswords\" and create an app password.Then put that password in the password field while logging in. \n2. Go to  \"https://www.google.com/settings/security/lesssecureapps\" and enable less secure apps permission"

def get_details(mailbox):
    # getting the mail list
    # rv, mailboxes = mail.list()
    # print mailboxes

    # getting emails from "INBOX"
    rv, data = mail.select(mailbox)
    if rv == 'OK':
        for num in data[0].split():
            rv, data = mail.fetch(num, '(RFC822)')
            if rv != 'OK':
                print "ERROR getting message", num

        # print data
        msg = email.message_from_string(data[0][1])
        email_ip = "Received"
        s = msg.get_all(email_ip)[1]
        ip = s[s.find("[")+1:s.find("]")]
        email_sender = "From"
        s = msg.get(email_sender)
        sender = s
        sender = sender.split(" <")
        sender[1] = sender[1].strip(">")
        mail.close()
        return ip,sender


def logout():
    print "\nLoging out..."
    mail.logout()
    print "Log out successful.\nHave a good day! :)"
