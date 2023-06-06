import firebase_admin
from firebase_admin import db


cred_obj = firebase_admin.credentials.Certificate('./private_key.json')
databaseURL = 'https://pythondbtest-88bb9-default-rtdb.firebaseio.com/'
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})


ref = db.reference("/Books/Best_Sellers/")
best_sellers = ref.get()
print(best_sellers)
for key, value in best_sellers.items():
	if(value['Author'] == 'J.R.R. Tolkien'):
		value["Price"] = 90
		ref.child(key).update({"Price":80})
        