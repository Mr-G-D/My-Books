import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open("images/books.png")
logo = logo.resize((round(logo.size[0]*0.25), round(logo.size[1]*0.25)))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=1)


student = tk.StringVar()
student_btn = tk.Button(root, textvariable=student, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
student.set("Students")
student_btn.grid(column=1, row=2)


books = tk.StringVar()
books_btn = tk.Button(root, textvariable=books, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
books.set("Books")
books_btn.grid(column=1, row=3)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)


root.mainloop()
