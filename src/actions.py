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

def to_books(dashboard):
    dashboard.destroy()
    from src.admin.books import books_table

def to_students(dashboard):
    dashboard.destroy()
    from src.admin.students import students_table




#STUDENTS

def to_students_index(index):
    index.destroy()
    from src.students.index import root

def to_students_login(index):
    index.destroy()
    from src.students.login import students_login

def to_students_register(index):
    index.destroy()
    from src.students.register import students_register

def students_login(data, frame):
    result = db.child('users').get()
    for element in result.each():
        if(data['email'] == element.val()['email'] and data['password'] == element.val()['password']):
            frame.destroy()
            from src.admin.books import books_table
            return(True)
    print(False)


def students_register(data, frame):
    db.child('users').push(data)
    frame.destroy()
    from src.admin.books import books_table