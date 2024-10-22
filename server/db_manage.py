import firebase_admin
from firebase_admin import credentials, firestore


PATH = "server/firebase_info.json"

def init_db():
    """
    make neccery initiolsations for the database
    """
    # Initialize the Firebase app with the service account key
    cred = credentials.Certificate(PATH)
    firebase_admin.initialize_app(cred)

    # Initialize Firestore
    db = firestore.client()
    return db

def get_files_from_db():
    """
    returns an array that contains a dictionary for each file in the database
    """
    db = init_db()
    files_collection = db.collection('files-hashes')
    docs = files_collection.stream()
    files = []
    for doc in docs:
        files.append(doc.to_dict())
    files.sort(key=lambda doc: doc.get("fileName"))
    return files