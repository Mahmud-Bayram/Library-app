from main import *

print("""***********************************

Welcome to the library application.

Processes:

1. Show Books

2. Book Inquiry

3. Add Book

4. Delete Book 

5. Edition Raise

Click 'q' for exit.
***********************************""")

library = Library()

while True:
    process = input("Your action:")

    if (process == "q"):
        print("The program is terminating.....")
        print("We wait again....")
        break
    elif (process == "1"):
        library.showBooks()

    elif (process == "2"):
        name = input("Which book do you want? ")
        print("Book inquiry...")
        time.sleep(2)

        library.inquiryBook(name)

    elif (process == "3"):
        name = input("Name:")
        author = input("Author:")
        publishingHouse= input("Publishing House:")
        type = input("Type:")
        edition = int(input("Edition:"))

        newBook = Book(name, author, publishingHouse, type, edition)

        print("Adding book....")
        time.sleep(2)

        library.addBook(newBook)
        print("Added book....")


    elif (process == "4"):
        name = input("Which book do you want to delete?")

        response = input("Are you sure? (Y/N)")
        if (response == "Y"):
            print("Deleting book...")
            time.sleep(2)
            library.deleteBook(name)
            print("Deleted book....")


    elif (process == "5"):
        isim = input("Which book's edition do you want to upgrade?")
        print("Upgrading edition....")
        time.sleep(2)
        library.raiseEdition(isim)
        print("Upgraded edition....")

    else:
        print("Invalid operation...")



