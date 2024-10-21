import firebase_admin
from firebase_admin import credentials, firestore

PATH = "server/firebase_info.json"


# Initialize the Firebase app with the service account key
cred = credentials.Certificate(PATH)
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# getting the data from the firestore database
hashes = db.collection('files-hashes')
docs = hashes.stream()
for doc in docs:
    print(doc.to_dict())