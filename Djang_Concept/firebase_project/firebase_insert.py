import firebase_admin
from firebase_admin import db
import json


cred_obj = firebase_admin.credentials.Certificate('./private_key.json')
databaseURL = 'https://pythondbtest-88bb9-default-rtdb.firebaseio.com/'
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})

ref = db.reference("/")

with open("book_info.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)

ref = db.reference("/Books/Best_Sellers")
ref.set({
	"Books":
	{
		"Best_Sellers": -1
	}
})

with open("book_info.json", "r") as f:
	file_contents = json.load(f)

for key, value in file_contents.items():
	ref.push().set(value)
