import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from src.actions import students_register as register

students_register = tk.Tk()
students_register.title('Students Register')
frame = ttk.Frame(students_register, width=600, height=300)
frame.grid( rowspan=3, columnspan=3)

ttk.Label(frame, text='students Register', font=("Raleway", 25), padding=10).grid(column=1, row=0)

ttk.Label(frame, text="Name", font=("Raleway", 15)).grid(column=1,row=3, pady=20)
students_name = tk.Entry(frame, bg="white", width=50)
students_name.grid(column=1, row=4)

ttk.Label(frame, text="Email-ID", font=("Raleway", 15)).grid(column=1,row=6, pady=20)
students_username = tk.Entry(frame, bg="white", width=50)
students_username.grid(column=1, row=7)


ttk.Label(frame, text="Password", font=("Raleway", 15)).grid(column=1,row=9, pady=20)
students_password = tk.Entry(frame, show="*", bg="white", width=50)
students_password.grid(column=1, row=10, pady=10)

def printValues():
    data = {
        'name': students_name.get(),
        'email': students_username.get(),
        'password': students_password.get()
    }
    register(data, students_register)

submit_register = tk.StringVar()
submit_btn = tk.Button(frame, textvariable=submit_register, command=lambda:printValues(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
submit_register.set("Register")
submit_btn.grid(column=1, row=15)

frame = tk.Frame(students_register, width=600, height=250)
frame.grid(rowspan=3, columnspan=3)

students_register.mainloop()

