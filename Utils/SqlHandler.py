import datetime
import os
import mysql.connector


# Get MySql Password
if os.path.isfile("password.txt"):
    with open("password.txt", "r") as f:
        PASSWORD = f.read()
else:
    PASSWORD = ""

if PASSWORD == "":
    PASSWORD = input("Enter MySql Password: ")
    with open("password.txt", "w") as f:
        f.write(PASSWORD)
        print("Password saved to password.txt")


# Connect to MySql

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=PASSWORD,
    database="book_shop_manager",
)
mycursor = mydb.cursor(buffered=True)


# Add Book
def AddBookToDB(name, price):
    name = name.title()
    mycursor.execute("INSERT INTO books (name, price) VALUES (%s, %s)", (name, price))
    mydb.commit()


# Update Book
def UpdateBookInDB(name, price):
    name = name.title()
    mycursor.execute(
        "UPDATE books SET price = %s WHERE name = %s",
        (price, name),
    )
    mydb.commit()


# Get Books
def GetBooksFromDB():
    mycursor.execute("SELECT * FROM books")
    dishes = mycursor.fetchall()
    return dishes


# Delete Book
def DeleteBookFromDB(name):
    name = name.title()
    mycursor.execute("DELETE FROM books WHERE name = %s", (name,))
    mydb.commit()


# Save Order
def SaveOrderInDB(PRICE):
    try:
        mycursor.execute("SELECT * FROM orders")
        ID = len(mycursor.fetchall()) + 1
    except:
        ID = 1

    DATE = datetime.datetime.date(datetime.datetime.now())
    mycursor.execute(
        "INSERT INTO orders (id,price,date) VALUES (%s,%s,%s)", (ID, PRICE, DATE)
    )
    mydb.commit()
    return ID, DATE


# Get Orders
def GetOrdersFromDB():
    mycursor.execute("SELECT * FROM orders")
    orders = mycursor.fetchall()
    return orders
