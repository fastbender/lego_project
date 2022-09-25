import mysql.connector

db = mysql.connector.connect (
	host="localhost",
	user="root",
	passwd="Sias2005",
	database="lego_items")

mycursor = db.cursor()

#mycursor.execute("DESCRIBE lego_items.lego_items_tbl")

#lego_items.`lego-db-csv220910`


mycursor.execute("SELECT * FROM lego_items.`lego-db-csv220910`")
for x in mycursor:
	print(x)
