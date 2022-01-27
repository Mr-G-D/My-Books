import requests

url = "https://api.itbook.store/1.0/new"

response = requests.get(url)

json_data = response.json()


# for element in json_data['books']:
#     print(element['title'])



from tkinter import *
from tkinter import ttk 

books_table = Tk()
books_table.title('Books')
canvas = Frame(books_table, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

my_books = ttk.Treeview(canvas)

my_books['columns'] = ('book_id','book_name', 'isbn', 'price')


my_books.column("#0", width=0,  stretch=NO)
my_books.column("book_id",anchor=CENTER,width=60)
my_books.column("book_name",anchor=CENTER, width=200)
my_books.column("isbn",anchor=CENTER,width=100)
my_books.column("price",anchor=CENTER,width=100)


my_books.heading("book_id",text="ID",anchor=CENTER)
my_books.heading("book_name",text="Book Name",anchor=CENTER)
my_books.heading("isbn",text="ISBN",anchor=CENTER)
my_books.heading("price",text="Price",anchor=CENTER)

count = 0
for element in json_data['books']:
    my_books.insert(parent='',index='end',iid=0,text='',values=(count+1,element['title'],element['isbn13'],element['price']))

my_books.grid(column=0, row=0, pady=10, padx=10)
books_table.mainloop()