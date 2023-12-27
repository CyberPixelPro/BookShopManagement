import mysql.connector
import os

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

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=PASSWORD,
    database="book_shop_manager",
)
mycursor = mydb.cursor()

BOOKS = [
    ("ENGLISH1", 759),
    ("ENGLISH2", 442),
    ("ENGLISH3", 704),
    ("HINDI1", 1560),
    ("HINDI2", 2560),
    ("HINDI3", 670),
    ("MATHS", 345),
    ("GEOGRAPHY", 425),
    ("CS", 565),
    ("PHYSICS", 734),
    ("CHEMISTRY", 687),
    ("ACCOUNTANCY", 425),
    ("PHYSICAL_EDUCATION", 475),
    ("ECONOMICS", 380),
    ("BIOLOGY", 549),
]


for book in BOOKS:
    try:
        mycursor.execute("INSERT INTO books (name, price) VALUES (%s, %s)", book)
    except Exception as e:
        print(e)
        print(f"Failed to insert {book}")

mydb.commit()
print("Successfully inserted books")
