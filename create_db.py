###################################################################################
# This script helps in connecting to the firebase realtime database and inserting #
# data in the same from the text files.                                           #
###################################################################################
import functions

firebase_db = functions.setUpFirebase()

# creating a list
def create_list(file_name, list_name):
    f = open(file_name, "r")
    a = f.readlines()
    for i in a:
        list_name.append(functions.formatDataForFirebase(i))

# creating a dictionary of spam words
def words_insert_data(arg):
    f = open("foofinal.txt", "r")
    a = f.readline()
    b = a.split(",")
    for i in b:
        arg[functions.formatDataForFirebase(i)] = 0

# inserting data into the database
def insert_in_db(col, ip_list, email_list, words_list, usernames_list):
    result = {
    "ip": ip_list,
    "email": email_list,
    "username": usernames_list,
    "words": words_list
    }
    firebase_db.set(result)

# dictionary to store all ips, emails and usernames in each, the key will be ip,
# email and usernames and values of these will be the number of times
# they appear in testing emails
ip = []
emails = []
usernames = []
words = {}

create_list("files/blocked_ip.txt", ip)
create_list("files/blocked_email.txt", emails)
create_list("files/blocked_username.txt", usernames)
words_insert_data(words)

insert_in_db(collection, ip, emails, words, usernames)
