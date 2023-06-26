import sqlite3

import time

class Book():

    def __init__(self, name, author, publishingHouse, type, edition):

        self.name = name
        self.author = author
        self.publishingHouse = publishingHouse
        self.type = type
        self.edition = edition

    def __str__(self):

        return "Book Name: {}\nAuthor: {}\nPublishing House: {}\nType: {}\nEdition: {}\n".format(self.name, self.author, self.publishingHouse, self.type, self.edition)


class Library():

    def __init__(self):

        self.buildingLink()

    def buildingLink(self):

        self.link = sqlite3.connect("library.db")

        self.cursor = self.link.cursor()

        query = "Create Table If not exists books (Name TEXT, Author TEXT, Publishing_house TEXT, Type TEXT, Edition INT)"

        self.cursor.execute(query)

        self.link.commit()


    def breakLink(self):

        self.link.close()


    def showBooks(self):

        query =  "Select * From books"

        self.cursor.execute(query)

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There are no books in the library...")
        else:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)

    def inquiryBook(self, name):

        query = "Select * From Books where Name = ?"

        self.cursor.execute(query, (name,))

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no such book.....")
        else:
            book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])

            print(book)
    def addBook(self, book):

        query = "Insert into Books Values(?,?,?,?,?)"

        self.cursor.execute(query, (book.name, book.author, book.publishingHouse, book.type, book.edition))

        self.link.commit()

    def deleteBook(self, name):

        query = "Delete From Books where Name = ?"

        self.cursor.execute(query, (name,))

        self.link.commit()

    def raiseEdition(self, name):

        query = "Select * From Books where Name = ?"

        self.cursor.execute(query, (name,))


        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is no such book...")
        else:
            edition = books[0][4]

            edition += 1

            query2 = "Update Books set Edition = ? where Name = ?"

            self.cursor.execute(query2, (edition, name))

            self.link.commit()
            
            
            
