from firebase_db import db


def admin_login(data, frame):
    result = db.child('admin').get()
    for element in result.each():
        if(data == element.val()):
            frame.destroy()
            from src.admin.dashboard import canvas
            return(True)
    print(False)

def to_admin_login(root):
    root.destroy()
    from src.admin.login import admin_login

