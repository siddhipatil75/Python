# Problem 1: Library System

class Book:
    def __init__(self, title):
        self.__title = title    # Encapsulation (private variable)
        self.__issued = False

    def get_title(self):
        return self.__title

    def is_issued(self):
        return self.__issued

    def issue(self):
        self.__issued = True

    def return_book(self):
        self.__issued = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_issued():
            book.issue()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.get_title()}")
        else:
            print(f"{book.get_title()} is already issued!")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.get_title()}")


# Inheritance - Student & Faculty
class Student(Member):
    def __init__(self, name):
        super().__init__(name)
        self.limit = 2   # Student borrowing limit


class Faculty(Member):
    def __init__(self, name):
        super().__init__(name)
        self.limit = 5   # Faculty borrowing limit


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            status = "Issued" if book.is_issued() else "Available"
            print(f"{book.get_title()} - {status}")


# --- Example Run ---
lib = Library()
b1 = Book("Python Basics")
b2 = Book("OOP in Python")

lib.add_book(b1)
lib.add_book(b2)

s1 = Student("Alice")
f1 = Faculty("Dr. Smith")

s1.borrow_book(b1)
f1.borrow_book(b1)  # Already issued
s1.return_book(b1)
f1.borrow_book(b1)

lib.show_books()


