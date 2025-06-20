"""

0. Dive into Python Magic Methods
mandatory
Objective: Master Python magic methods by implementing a Book class that incorporates constructors (__init__), destructors (__del__), and the representation methods (__str__ and __repr__).

Task Description:
Create a Python script named book_class.py. In this script, define a Book class that uses specific magic methods to enhance its functionality. This class will model a book with attributes for the title, author, and publication year.

Requirements for Book Class in book_class.py:
Attributes:

title (str): The title of the book.
author (str): The author of the book.
year (int): The publication year of the book.
Magic Methods:

Constructor (__init__): Initializes a Book instance with title, author, and year.
Destructor (__del__): Prints "Deleting (title of the book)" upon object deletion.
String Representation (__str__): Returns a string in the format "(title) by (author), published in (year)".
Official Representation (__repr__): Returns a string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})".
Provided for Testing: main.py
To test your Book class, use the following main.py script, which demonstrates creating a Book instance and utilizing the implemented magic methods:

from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
Expected Output:
1984 by George Orwell, published in 1949
Book('1984', 'George Orwell', 1949)
Deleting 1984

"""

#by Gemini

# book_class.py
# book_class.py

class Book:
    """
    Represents a book with a title, author, and publication year.
    Demonstrates the use of Python's magic methods:
    __init__, __del__, __str__, and __repr__.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor for the Book class.
        Initializes a new Book instance with the given title, author, and year.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        # Removed: print(f"Book '{self.title}' created.") - This line caused the extra output.

    def __del__(self):
        """
        Destructor for the Book class.
        This method is called when the object is about to be destroyed (deleted).
        It prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns the informal string representation of the Book object.
        This is typically used for end-user display (e.g., by the print() function).

        Returns:
            str: A formatted string: "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official (developer-facing) string representation of the Book object.
        This string should ideally be unambiguous and allow recreation of the object.

        Returns:
            str: A string that would recreate the Book instance:
                 f"Book('{self.title}', '{self.author}', {self.year})"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

