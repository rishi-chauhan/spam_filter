"""
This script helps in connecting to the firebase realtime database and inserting
data in the same from the text files
"""
import functions

FIREBASE_DB = functions.set_up_firebase()
# dictionary to store all ips, emails and usernames in each, the key will be ip,
# email and usernames and values of these will be the number of times
# they appear in testing emails
IP = []
EMAILS = []
USERNAMES = []
WORDS = {}

def create_list(file_name, list_name):
    """creates a list"""
    f = open(file_name, "r")
    a = f.readlines()
    for i in a:
        list_name.append(functions.format_data_for_firebase(i))

def words_insert_data(arg):
    """creates a dictionary of spam words"""
    f = open("foofinal.txt", "r")
    a = f.readline()
    b = a.split(",")
    for i in b:
        arg[functions.format_data_for_firebase(i)] = 0

def insert_in_db(ip_list, email_list, words_list, usernames_list):
    """inserts data into the database"""
    result = {
        "ip": ip_list,
        "email": email_list,
        "username": usernames_list,
        "words": words_list
    }
    FIREBASE_DB.set(result)

create_list("files/blocked_ip.txt", IP)
create_list("files/blocked_email.txt", EMAILS)
create_list("files/blocked_username.txt", USERNAMES)
words_insert_data(WORDS)

insert_in_db(IP, EMAILS, WORDS, USERNAMES)
