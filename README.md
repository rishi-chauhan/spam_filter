# The Project
  spam filter project

# How does it works?
  create_db.py file creates a Firebase Realtime Database. This takes data from files from files folder.
  functions.py contains common functions used across the project.
  import_from_mongo_to_firebase.py helps in transfer data from local MongoDB database to Firebase.
  main.py contains the main code which connects to the email server of user and gets the latest email. This then analyses the email and marks it as spam or not.
  update_db.py connects to the spam folder of the user's email account and updates Firebase Realtime Database for spam IPs, usernames and spam words.

Project is on hold
