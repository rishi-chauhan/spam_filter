#################################################################################
#This script helps in connecting to the database and inserting data in the same.#
#################################################################################

# from pymongo import MongoClient
import pyrebase         # for firebase

# config firebase for app
config = {
    "apiKey": "AIzaSyD6oXg-aMBIZ_rK6aSW9uZZcI4ITk_zZJM",
    "authDomain": "spam-filter-e2306.firebaseapp.com",
    "databaseURL": "https://spam-filter-e2306.firebaseio.com",
    "projectId": "spam-filter-e2306",
    "storageBucket": "spam-filter-e2306.appspot.com",
    "messagingSenderId": "438892013228"
  }

# client = MongoClient()

# connecting to db
# db = client.project

# creating a collection
# collection = db.spam

# creating a list
def create_list(file_name, list_name):
    f = open(file_name, "r")
    a = f.readlines()
    for i in a:
        list_name.append(i.strip("\n"))

# creating a dictionary of spam words
def words_insert_data(arg):
    f = open("foofinal.txt", "r")
    a = f.readline()
    b = a.split(",")
    for i in b:
        arg[i] = 0


# initialise firebase connection
firebase = pyrebase.initialize_app(config)

# connect to database
db = firebase.database()

# inserting data into the database
def insert_in_db(col, ip_list, email_list, words_list, usernames_list):
    result = {
    "ip": ip_list,
    "email": email_list,
    "username": usernames_list,
    "words": words_list
    }
    db.set(result)

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
