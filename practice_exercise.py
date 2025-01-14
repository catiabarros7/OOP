class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}"


class Member:
    def __init__ (self, name, memberID):
        self.name = name
        self.memberID = memberID
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name} (ID: {self.memberID})"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def lend_book(self, book, member):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print(f"{book.title} has been lent to {member.name}")
        
        else:
            print(f"Sorry, {book.title} is not available for lending")

    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"{book.title} has been returned by {member.name}")

        else:
            print(f"{member.name} did not borrow {book.title}")


book1 = Book("The Girl You Killed", "Leslie Wolfe")
book2 = Book("Equador", "Miguel Sousa Tavares")

member1 = Member("Esmeralda", 5001)
member2 = Member("Denise", 5002)

Library = Library()

Library.add_book(book1)
Library.add_book(book2)

Library.register_member(member1)
Library.register_member(member2)

Library.lend_book(book1, member1)
Library.lend_book(book2, member2)
Library.return_book(book1, member1)
Library.return_book(book2, member1) # This will fail becuase book2 is not borrowed by member1