"""
1. Mastering Inheritance and Composition in Python
mandatory
Objective: Deepen your understanding of inheritance and composition in Python by creating a system that models a library with different types of books.

Task Description:
Develop two Python scripts: library_system.py and main.py. In library_system.py, you’ll define a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance. Additionally, implement a Library class demonstrating composition by managing a collection of books.

library_system.py:
Base Class - Book:

Attributes: title (str) and author (str).
Method: __init__(self, title, author) for initializing book attributes.
Derived Classes - EBook and PrintBook:

Both classes inherit from Book.
EBook additional attribute: file_size (int).
PrintBook additional attribute: page_count (int).
Each derived class should have its own __init__ method that properly calls the base class __init__ while also initializing its unique attribute.
Composition - Library:

Attributes: books (a list to store instances of Book, EBook, and PrintBook).
Methods:
add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
list_books(self): Prints details of each book in the library.
main.py (Provided for Testing):
This script tests the functionality of your classes in library_system.py by adding different types of books to a Library instance and listing them.

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
Expected Output:
Your output should list the details of each book added to the library, reflecting the specific attributes of EBook and PrintBook, as well as the common attributes inherited from Book.

Book: Pride and Prejudice by Jane Austen
EBook: Snow Crash by Neal Stephenson, File Size: 500KB
PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234

"""

#by Gemini

# library_system.py
# library_system.py

class Book:
    """
    Base class representing a generic book.
    Attributes: title (str), author (str).
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Derived class representing an electronic book, inheriting from Book.
    Additional attribute: file_size (int).
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes an EBook instance.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The file size of the e-book in KB.
        """
        super().__init__(title, author) # Call the base class (Book) constructor
        self.file_size = file_size

    def __str__(self):
        """
        Returns a user-friendly string representation of the EBook,
        including file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Derived class representing a print book, inheriting from Book.
    Additional attribute: page_count (int).
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author) # Call the base class (Book) constructor
        self.page_count = page_count

    def __str__(self):
        """
        Returns a user-friendly string representation of the PrintBook,
        including page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Class demonstrating composition, managing a collection of books.
    Attributes: books (list) - stores instances of Book, EBook, and PrintBook.
    """
    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a Book, EBook, or PrintBook instance to the library's collection.

        Args:
            book (Book): An instance of Book or its derived classes.
        """
        self.books.append(book)
        # Removed: print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        It leverages the __str__ method of each book object.
        """
        # Removed: print("\n--- Books in the Library ---")
        # Removed: if not self.books:
        # Removed:     print("The library is currently empty.")
        for book in self.books:
            print(book) # This will automatically call the appropriate __str__ method
        # Removed: print("----------------------------")

