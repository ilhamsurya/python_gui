from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

def populate_list():
  products_list.delete(0,END)
  for row in db.fetch():
    products_list.insert(END, row)

def add_product():
    if product_text.get() == '' or customer_text.get() == '' or shop_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required', 'Please Fill All Field')
        return
    db.insert(product_text.get(), customer_text.get(), shop_text.get(),price_text.get())
    products_list.delete(0,END)
    products_list.insert(END, (product_text.get(), customer_text.get(), shop_text.get(),price_text.get()))
    clear_input()
    populate_list()

# making the removal is possible (response)
def select_item(event):
    try:
        global selected_item
        index = products_list.curselection()[0]
        selected_item = products_list.get(index)
        print(selected_item)

        product_entry.delete(0, END)
        product_entry.insert(END, selected_item[1])
        
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        
        shop_entry.delete(0, END) 
        shop_entry.insert(END, selected_item[3])
        
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_product():
    db.remove(selected_item[0])
    clear_input()
    populate_list()

def update_product():
    db.update(selected_item[0], product_text.get(), customer_text.get(), shop_text.get(),price_text.get())
    populate_list()

def clear_input():
    product_entry.delete(0, END)
    customer_entry.delete(0, END)
    shop_entry.delete(0, END)
    price_entry.delete(0, END)
   
#create window 
app = Tk()

#Product 
product_text = StringVar()
product_label= Label(app, text = 'Product Name: ', font = ('Bold', 15), pady=10)
product_label.grid(row = 0, column = 0, sticky = W)
product_entry = Entry(app, textvariable=product_text)
product_entry.grid(row = 0, column = 1) 

#customer
customer_text = StringVar()
customer_label= Label(app, text = 'Customer Name: ', font = ('Bold', 15), pady=10)
customer_label.grid(row = 0, column = 2, sticky = W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row = 0, column = 3) 
 
#Shop
shop_text = StringVar()
shop_label= Label(app, text = 'Shop: ', font = ('Bold', 15), pady=10)
shop_label.grid(row = 1, column = 0, sticky = W)
shop_entry = Entry(app, textvariable=shop_text)
shop_entry.grid(row = 1, column = 1) 

#Price
price_text = StringVar()
price_label= Label(app, text = 'Price: ', font = ('Bold', 15), pady=10)
price_label.grid(row = 1, column = 2, sticky = W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row = 1, column = 3) 

#product list
products_list = Listbox(app,height = 8, width = 50, border = 0)
products_list.grid(row = 3, column = 0, columnspan = 2, rowspan = 4, padx = 20, pady = 20)

#scroll bar
scrollbar = Scrollbar(app)
scrollbar.grid(row = 3, column = 3)

#set scroll to listbox
products_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command=products_list.yview)

#Bind Select
products_list.bind('<<ListboxSelect>>', select_item)

#buttons add product
add_btn = Button(app, text="add product", width=12, command=add_product)
add_btn.grid(row=2,column=0,pady=25)


#buttons remove product
remove_btn = Button(app, text="remove product", width=12, command=remove_product)
remove_btn.grid(row=2,column=1)


#buttons update product
update_btn = Button(app, text="Update product", width=12, command=update_product)
update_btn.grid(row=2,column=2)
 

#buttons add product
clear_btn = Button(app, text="Clear input", width=12, command=clear_input)
clear_btn.grid(row=2,column=3)


app.title('Toko Serba Ada')
app.geometry('700x350')

#populate data
populate_list()

#start 
app.mainloop()