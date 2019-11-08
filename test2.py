# coding=utf-8

class Book:
#I metoden __init__ definierar vi objektets attribut och ger dom värden.
    def __init__(self, title, author, pages, isbn = "-"):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
            
sport = Book("Newcastle", "Jonas Lindberg", 360, "0-224-02040-4")

print(sport)
