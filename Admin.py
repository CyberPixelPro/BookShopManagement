from Utils.BillHandler import GetBillText
from Utils.SqlHandler import (
    AddBookToDB,
    DeleteBookFromDB,
    GetBooksFromDB,
    GetOrdersFromDB,
    UpdateBookInDB,
)

# Menu for Admin


def showMenu():
    print()
    print("==================================".center(100))
    print("Rahul Book Store".center(100))
    print("==================================".center(100))
    print()
    print("ADMIN MENU".center(100))
    print()
    print(" " * 25 + "1. Add New Book")
    print(" " * 25 + "2. Update Book")
    print(" " * 25 + "3. Show Books")
    print(" " * 25 + "4. Delete Book")
    print(" " * 25 + "5. Show Orders")
    print(" " * 25 + "6. Show Bills")
    print(" " * 25 + "7. Show Income")
    print(" " * 25 + "0. Exit")
    print()

    choice = int(input(">> Enter your choice: "))
    if choice == 1:
        addBook()
    elif choice == 2:
        updateBook()
    elif choice == 3:
        showBooks()
    elif choice == 4:
        deleteBook()
    elif choice == 5:
        showOrders()
    elif choice == 6:
        showBills()
    elif choice == 7:
        showIncome()
    elif choice == 0:
        print()
        print("Exiting...")
        exit()
    else:
        print("Invalid Choice")
        print()
        input("Press Enter To Open Menu...")

    showMenu()


# Fucntions for Admin Menu


def addBook():
    print()
    print("============".center(100))
    print("Add New Book".center(100))
    print("============".center(100))
    print()
    NAME = input("Enter Book Name: ")
    PRICE = int(input("Enter Book Price: "))
    AddBookToDB(NAME, PRICE)
    print()
    print(">> Book Added Successfully")
    print()
    input("Press Enter To Open Menu...")


def updateBook():
    print()
    print("===========".center(100))
    print("Update Book".center(100))
    print("===========".center(100))
    print()
    NAME = input("Enter Book Name: ")
    PRICE = int(input("Enter Book Price: "))
    UpdateBookInDB(NAME, PRICE)
    print()
    print(">> Book Updated Successfully")
    print()
    input("Press Enter To Open Menu...")


def showBooks():
    print()
    print("================".center(100))
    print("Available Books".center(100))
    print("================".center(100))
    print()

    print("=" * 100)
    print("|| ID ||" + "BOOK".center(50) + "||" + "PRICE".center(38) + "||")
    print("=" * 100)

    BOOKS = GetBooksFromDB()
    pos = 1
    for book, price in BOOKS:
        print(
            "||"
            + str(pos).center(4)
            + "||"
            + book.title().center(50)
            + "||"
            + (str(price) + " ₹").center(38)
            + "||"
        )
        pos += 1
    print("=" * 100)

    print()
    input("Press Enter To Open Menu...")


def deleteBook():
    print()
    print("===========".center(100))
    print("Delete Book".center(100))
    print("===========".center(100))
    print()
    NAME = input("Enter Book Name: ")
    DeleteBookFromDB(NAME)
    print()
    print(">> Book Deleted Successfully")
    print()
    input("Press Enter To Open Menu...")


def showOrders():
    print()
    print("===========".center(100))
    print("All Orders".center(100))
    print("===========".center(100))
    print()

    ORDERS = GetOrdersFromDB()

    print("=" * 100)
    print("|| ID ||" + "TOTAL PRICE".center(50) + "||" + "DATE".center(38) + "||")
    print("=" * 100)

    for ID, PRICE, DATE in ORDERS:
        print(
            "||"
            + str(ID).center(4)
            + "||"
            + (str(PRICE) + " ₹").center(50)
            + "||"
            + str(DATE).center(38)
            + "||"
        )
    print("=" * 100)

    print()
    input("Press Enter To Open Menu...")


def showBills():
    print()
    print("=========================".center(100))
    print("Select Order To View Bill".center(100))
    print("=========================".center(100))
    print()

    ORDERS = GetOrdersFromDB()

    print("=" * 100)
    print("|| ID ||" + "TOTAL PRICE".center(50) + "||" + "DATE".center(38) + "||")
    print("=" * 100)

    IDS = []
    for ID, PRICE, DATE in ORDERS:
        IDS.append(ID)
        print(
            "||"
            + str(ID).center(4)
            + "||"
            + (str(PRICE) + " ₹").center(50)
            + "||"
            + str(DATE).center(38)
            + "||"
        )
    print("=" * 100)

    print()

    while True:
        try:
            ORDER_ID = int(input(">> Enter Order ID: "))
            print()
        except:
            print("Invalid Order ID")
            print()
            continue

        if ORDER_ID in IDS:
            break
        else:
            print("Invalid Order ID")
            print()
            continue

    BILL_FILE, BILL_TEXT = GetBillText(ORDER_ID, ORDERS[IDS.index(ORDER_ID)][2])
    print(f"Opening Bill File: {BILL_FILE}\n")
    print(BILL_TEXT)
    print()
    input("Press Enter To Open Menu...")


def showIncome():
    ORDERS = GetOrdersFromDB()
    TOTAL = 0
    for ID, PRICE, DATE in ORDERS:
        TOTAL += PRICE

    print()
    print(f">> Total Income: {TOTAL} ₹")
    print()
    input("Press Enter To Open Menu...")


# Start The Program
if __name__ == "__main__":
    while True:
        try:
            showMenu()
        except KeyboardInterrupt:
            print()
            print("Exiting...")
            exit()
        except Exception as e:
            print("Error:", e)
            print()
            input("Press Enter To Open Menu...")
