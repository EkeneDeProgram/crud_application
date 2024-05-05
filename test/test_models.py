import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from app.models import Book


class TestBookModel(unittest.TestCase):
    """
    Test case to verify that a Book instance is correctly initialized
    with the provided attributes.
    """

    def test_book_attributes(self):
        # Create a new book instance
        book = Book(
            title="Sample Book", author="Sample Author", year=2022, isbn="1234567890"
        )

        # Assert that the book attributes are set correctly
        self.assertEqual(book.title, "Sample Book")
        self.assertEqual(book.author, "Sample Author")
        self.assertEqual(book.year, 2022)
        self.assertEqual(book.isbn, "1234567890")


if __name__ == "__main__":
    unittest.main()
