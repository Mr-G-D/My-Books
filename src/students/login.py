import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from src.actions import students_login as login

students_login = tk.Tk()
 
frame = ttk.Frame(students_login, width=600, height=300)
frame.grid( rowspan=3, columnspan=3)

ttk.Label(frame, text='students Login', font=("Raleway", 25), padding=10).grid(column=1, row=0)

ttk.Label(frame, text="Email-ID", font=("Raleway", 15)).grid(column=1,row=3, pady=20)
students_username = tk.Entry(frame, bg="white", width=50)
students_username.grid(column=1, row=4)


ttk.Label(frame, text="Password", font=("Raleway", 15)).grid(column=1,row=6, pady=20)
students_password = tk.Entry(frame, show="*", bg="white", width=50)
students_password.grid(column=1, row=7, pady=10)

def printValues():
    data = {
        'email': students_username.get(),
        'password': students_password.get()
    }
    login(data, students_login)

submit_login = tk.StringVar()
submit_btn = tk.Button(frame, textvariable=submit_login, command=lambda:printValues(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
submit_login.set("Submit")
submit_btn.grid(column=1, row=15)

frame = tk.Frame(students_login, width=600, height=250)
frame.grid(rowspan=3, columnspan=3)

students_login.mainloop()

