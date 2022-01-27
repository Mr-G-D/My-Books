from firebase_db import db


def admin_login(data):
    result = db.child('admin').get()
    for element in result.each():
        if(data == element.val()):
            print(True)
            break
    print(False)

def to_admin_login(root):
    root.destroy()
    from src.admin.login import admin_login

