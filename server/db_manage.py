import firebase_admin
from firebase_admin import credentials, firestore

PATH = "server/firebase_info.json"


def get_files_from_db(db):
    """returns an array that contains a dictionary for each file in the database"""
    files_collection = db.collection('files-hashes')
    docs = files_collection.stream()
    files = []
    for doc in docs:
        files.append(doc.to_dict())
    return files

def main():
    # Initialize the Firebase app with the service account key
    cred = credentials.Certificate(PATH)
    firebase_admin.initialize_app(cred)

    # Initialize Firestore
    db = firestore.client()

    files = get_files_from_db(db)