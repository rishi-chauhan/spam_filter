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

# initialise firebase connection
firebase = pyrebase.initialize_app(config)

# connect to database
db = firebase.database()

data = {"users":{"u1": {"music": "test1"}}}

db.set(data)
