from firebase_db import db


def admin_login(data):
    db.child('admin').push(data)

def to_admin_login(root):
    root.destroy()
    from src.admin.login import admin_login

