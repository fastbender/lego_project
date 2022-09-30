# ken6.py
# this uses tkinter to handle display and treeview
# 

from tkinter import *
from tkinter import ttk  # need for treeview
from tkinter import messagebox
from PIL import ImageTk, Image

import mysql.connector
import tkinter as tk

# setup our database
db = mysql.connector.connect (
	host="localhost",
	user="root",
	passwd="Sias2005",
	database="lego_items")

my_cursor = db.cursor()

root = tk.Tk()
root.title('Lego sets and Mini Figures')
root.geometry ("1000x600")

# add some style
style = ttk.Style()
style.theme_use('default')

# configure the Treeview colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# set the color of Selected row
style.map('TreeView',
	background=[('selected',"#347083")])

# create the frame to hold the Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)   # this makes the frame slightly down from the top of the screen

# create a scroll bar for the treeview
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# let create the actual Treeview now
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=15)
my_tree.pack() 


# configure the scroll bar
tree_scroll.config(command=my_tree.yview)

#define the colums in the treeview
my_tree['columns'] = ("Catalog #", "Category", "Title", "Original $", "TaoBao $", "Owned by", "Status", "First Year", "Last Year")

# lets format our columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Catalog #", anchor=E, width=70)
my_tree.column("Category", anchor=W, width=140)
my_tree.column("Title", anchor=W, width=400)
my_tree.column("Original $", anchor=E, width=70)
my_tree.column("TaoBao $", anchor=E, width=70)
my_tree.column("Owned by", anchor=W, width=110)
my_tree.column("Status", anchor=W, width=110)
my_tree.column("First Year", anchor=W, width=110)
my_tree.column("Last Year", anchor=W, width=110)

# lets add the title to the columns
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Catalog #", text="Catalog #", anchor=W)
my_tree.heading("Category", text="Category", anchor=W)
my_tree.heading("Title", text="Title", anchor=W)
my_tree.heading("Original $", text="Orginal $", anchor=W)
my_tree.heading("TaoBao $", text="TaoBao $", anchor=W)
my_tree.heading("Owned by", text="Owned by", anchor=W)
my_tree.heading("Status", text="Status", anchor=W)
my_tree.heading("First Year", text="First Year", anchor=W)
my_tree.heading("Last Year", text="Last Year", anchor=W)

# setup rows to be Striped
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# run the SQL query and get the results
my_cursor.execute("SELECT * FROM lego_items.`lego-db-csv220910` ORDER BY cat_number")

results = my_cursor.fetchall()
	

# Add our data to the screen
global count
count = 0

for record in results:
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[5], record[6], record[7], record[9], record[2], record[8], record[3], record[4]), tags=('evenrow',))
	else:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[5], record[6], record[7], record[9], record[2], record[8], record[3], record[4]), tags=('oddrow',))
	# increment counte
	count += 1



# Clear Text Fields
def clear_fields():
	catalog_number_entry.delete(0, END)
	category_entry.delete(0, END)
	title_entry.delete(0, END)
	original_price_entry.delete(0, END)
	taobao_price_entry.delete(0, END)
	owned_by_entry.delete(0, END)
	item_retired_entry.delete(0, END)
	first_year_entry.delete(0, END)
	last_year_entry.delete(0, END)

# Select Record
def select_record(e):
	# clear entry fields
	clear_fields()

	# Grab record number
	selected = my_tree.focus()

	# Grab record valuses
	values = my_tree.item(selected, 'values')

	# Put data into fields
	catalog_number_entry.insert(0, values[0])
	category_entry.insert(0, values[1])
	title_entry.insert(0, values[2])
	original_price_entry.insert(0, values[3])
	taobao_price_entry.insert(0, values[4])
	owned_by_entry.insert(0, values[5])
	item_retired_entry.insert(0, values[6])
	first_year_entry.insert(0, values[7])
	last_year_entry.insert(0, values[8])


#    pictItem = "Legoimages"+catalog_number_entry+".png"
#    pictBox  = "Legoimages"+catalog_number_entry+"box.png"



# Add Record To Database
def add_record():
#	sql_command = "INSERT INTO lego_items.`lego-db-csv220910` (cat_number, category, title, orginal_price, taobao_price, owned_by, item_retired, first_year, last_year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)" values = (category_entry.get(), title_entry.get(), orginal_price_entry.get(), taobao_price_entry.get(), owned_by_entry.get(), item_retired_entry.get(), first_year_entry.get(), last_year_entry.get())

	sql_command = "INSERT INTO lego_items.`lego-db-csv220910` (cat_number, category, title, original_price, taobao_price, owned_by, item_retired, first_year, last_year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)" 
	values = (catalog_number_entry.get(), category_entry.get(), title_entry.get(), original_price_entry.get(), taobao_price_entry.get(), owned_by_entry.get(), item_retired_entry.get(), first_year_entry.get(), last_year_entry.get())

	#print (sql_command)
	#print (values)

	my_cursor.execute(sql_command, values)

	# Commit the changes to the database
	db.commit()
	# Clear the fields
	clear_fields()


def delete_record():
	x = my_tree.selection()[0]
	my_tree.delete(x)


	my_cursor.execute("DELETE from lego_items.`lego-db-csv220910` WHERE cat_number=" + catalog_number_entry.get())

	# Commit the changes to the database
	db.commit()
	# Clear the fields
	clear_fields()

	# display message box saying the record was delete
	messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")


def update_record():
#	sql_command 
	sql_command = """UPDATE lego_items.`lego-db-csv220910` SET 
	cat_number = %s, 
	category = %s, 
	title = %s, 
	original_price = %s, 
	taobao_price = %s, 
	owned_by = %s, 
	item_retired = %s, 
	first_year = %s, 
	last_year = %s 
	WHERE cat_number = %s"""
		
	cat_number = catalog_number_entry.get()
	category = category_entry.get()
	title = title_entry.get()
	original_price = original_price_entry.get()
	taobao_price = taobao_price_entry.get()
	owned_by = owned_by_entry.get()
	item_retired = item_retired_entry.get()
	first_year = first_year_entry.get()
	last_year = last_year_entry.get()

	input = (cat_number, category, title, original_price, taobao_price, owned_by, item_retired, first_year, last_year, cat_number)
	my_cursor.execute(sql_command, input)

	# Commit the changes to the database
	db.commit()




# create two frames below of the Treeview
middle_frame = LabelFrame(root, text="Record")
middle_frame.pack(fill="x", expand="yes", padx=20)


# Add Image

# my_image = ImageTk.PhotoImage(Image.open("Lego_images\\Lego75342.png"))
# image_label = Label(image=my_image)

# Create a photoimage object of the image in the path
image1 = Image.open("Lego_images\\Lego7499box-thm.png")
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test

# Position image
#label1.place(x=1, y=2)





# Add Record Entry Boxes
# first line of entry boxes and titles
catalog_number_label = Label(middle_frame, text="Catalog #")
catalog_number_label.grid(row=0, column=0, padx=10, pady=10)
catalog_number_entry = Entry(middle_frame)
catalog_number_entry.grid(row=0, column=1, padx=10, pady=10)

category_label = Label(middle_frame, text="Category")
category_label.grid(row=0, column=2, padx=10, pady=10)
category_entry = Entry(middle_frame)
category_entry.grid(row=0, column=3, padx=10, pady=10)

title_label = Label(middle_frame, text="Title")
title_label.grid(row=0, column=4, padx=10, pady=10, sticky='w')
title_entry = Entry(middle_frame, width=110)
title_entry.grid(row=0, column=5, padx=10, pady=10)


# second line of entry boxes and titles
original_price_label = Label(middle_frame, text="Original $")
original_price_label.grid(row=1, column=0, padx=10, pady=10)
original_price_entry = Entry(middle_frame,justify=RIGHT)
original_price_entry.grid(row=1, column=1, padx=10, pady=10)

taobao_price_label = Label(middle_frame, text="TaoBao $")
taobao_price_label.grid(row=1, column=2, padx=10, pady=10)
taobao_price_entry = Entry(middle_frame, justify=RIGHT)
taobao_price_entry.grid(row=1, column=3, padx=10, pady=10)

owned_by_label = Label(middle_frame, text="Owned By")
owned_by_label.grid(row=1, column=4, padx=10, pady=10, sticky='w')
owned_by_entry = Entry(middle_frame)
owned_by_entry.grid(row=1, column=5, padx=10, pady=10, sticky='w')



# third line of entry boxes and titles
first_year_label = Label(middle_frame, text="First Year")
first_year_label.grid(row=2, column=0, padx=10, pady=10)
first_year_entry = Entry(middle_frame)
first_year_entry.grid(row=2, column=1, padx=10, pady=10)

last_year_label = Label(middle_frame, text="Last Year")
last_year_label.grid(row=2, column=2, padx=10, pady=10)
last_year_entry = Entry(middle_frame)
last_year_entry.grid(row=2, column=3, padx=10, pady=10)

item_retired_label = Label(middle_frame, text="Status")
item_retired_label.grid(row=2, column=4, padx=10, pady=10, sticky='w')
item_retired_entry = Entry(middle_frame)
item_retired_entry.grid(row=2, column=5, padx=10, pady=10, sticky='w')

# Add action buttons
button_frame = LabelFrame(root, text="Logo")
button_frame.pack(fill="x", expand="yes", padx=20)

add_button = Button(button_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=1, padx=10, pady=10)

delete_button = Button(button_frame, text="Delete Record", command=delete_record)
delete_button.grid(row=0, column=2, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entry Fields", command=clear_fields)
select_record_button.grid(row=0, column=4, padx=10, pady=10)



# bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

#select record
def select_record(e):
	selected = my_tree.focus()

#grab the values of the selected item
	values = my_tree.item(selected, 'values')



root.mainloop()