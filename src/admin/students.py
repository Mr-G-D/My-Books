from firebase_db import db

result = db.child('users').get()

# students = []
for element in result.each():
    print(element.val()['email'])


from tkinter import *
from tkinter import ttk 

students_table = Tk()
students_table.title('Students')
canvas = Frame(students_table, width=600, height=500)
canvas.grid(columnspan=3, rowspan=3)

students = ttk.Treeview(canvas, height=20)

students['columns'] = ('students_id','students_name')


students.column("#0", width=0,  stretch=NO)
students.column("students_id",anchor=CENTER,width=100)
students.column("students_name",anchor=CENTER, width=240)


students.heading("students_id",text="ID",anchor=CENTER)
students.heading("students_name",text="Students Name",anchor=CENTER)

count = 0
for element in result.each():
    count+=1
    students.insert(parent='',index='end',iid=count,text='',values=(count,element.val()['email']))

students.grid(column=0, row=0, pady=10, padx=10)
students_table.mainloop()