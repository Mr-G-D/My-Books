from firebase import Firebase
from config import config



firebase = Firebase(config)

db = firebase.database()

