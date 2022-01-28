import tkinter as tk
from PIL import Image, ImageTk
from firebase_db import db
from src.actions import to_students_login, to_students_register


root = tk.Tk()

students_index = tk.Canvas(root, width=600, height=300)
students_index.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open("images/books.png")
logo = logo.resize((round(logo.size[0]*0.25), round(logo.size[1]*0.25)))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=1)


register = tk.StringVar()
register_btn = tk.Button(root, textvariable=register, command=lambda:to_students_register(root), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
register.set("Register")
register_btn.grid(column=1, row=2)


login = tk.StringVar()
login_btn = tk.Button(root, textvariable=login, command=lambda:to_students_login(root), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
login.set("Login")
login_btn.grid(column=1, row=3)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)


root.mainloop()
