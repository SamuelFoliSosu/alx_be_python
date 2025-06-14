"""

3. Implementing Basic OOP for a Library Management System
mandatory
Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.

Your Task: library_management.py
Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.
Provided for Testing: main.py
This script demonstrates how to interact with your Book and Library classes.

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
Expected Outputs for Each Step in main.py:
After Initial Setup:
   Available books after setup:
   Brave New World by Aldous Huxley
   1984 by George Orwell
After Checking Out ‘1984’:
   Available books after checking out '1984':
   Brave New World by Aldous Huxley
After Returning ‘1984’:
   Available books after returning '1984':
   Brave New World by Aldous Huxley
   1984 by George Orwell
Note for you:
Your Book class should provide methods to check a book out and return it, affecting its availability.
Your Library class needs to manage a collection of books, including adding new books to the collection, checking a book out (which marks it as unavailable), returning it (making it available again), and listing all available books.
Implementing these functionalities requires careful thought about how objects interact with each other in terms of state and behavior.
Use the provided main.py for testing your implementation. The expected outputs give you a clear indication of how your program should behave if implemented correctly.

"""

# library_management.py by Gemni

class Book:
    """
    Represents a book in the library with its title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title       # Public attribute
        self.author = author     # Public attribute
        self._is_checked_out = False # Private attribute (conventionally indicated by single underscore)

    def check_out(self):
        """
        Marks the book as checked out if it's currently available.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False # Already checked out

    def return_book(self):
        """
        Marks the book as available if it's currently checked out.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False # Already available

    def is_available(self):
        """
        Checks if the book is currently available.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects, allowing adding, checking out,
    returning, and listing available books.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list to store books.
        """
        self._books = [] # Private list to store Book instances

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): An instance of the Book class to be added.
        """
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added '{book.title}' to the library.")
        else:
            print("Error: Only Book objects can be added to the library.")

    def check_out_book(self, title):
        """
        Finds a book by its title and attempts to check it out.

        Args:
            title (str): The title of the book to check out.

        Returns:
            bool: True if the book was found and successfully checked out, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"Error: Book with title '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """
        Finds a book by its title and attempts to return it.

        Args:
            title (str): The title of the book to return.

        Returns:
            bool: True if the book was found and successfully returned, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return True
                else:
                    print(f"'{title}' is already available.")
                    return False
        print(f"Error: Book with title '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """
        Prints the title and author of all books currently available in the library.
        If no books are available, it prints a corresponding message.
        """
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book) # Uses the __str__ method of the Book class
                available_count += 1
        if available_count == 0:
            print("No books are currently available.")

