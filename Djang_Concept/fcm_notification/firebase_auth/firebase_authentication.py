import os 
import firebase_admin
from firebase_admin import credentials



cred_obj = firebase_admin.credentials.Certificate('./private_key.json')
databaseURL = 'https://pythondbtest-88bb9-default-rtdb.firebaseio.com/'
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})


