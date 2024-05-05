import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from app.schemas import BookBase, BookUpdate, BookCreate, BookInDB


class TestBookModels(unittest.TestCase):
    def test_book_base(self):
        """
        Test case to verify the attributes of the BookBase class.
        It creates a new instance of the BookBase class using sample book data.
        """
        # Define sample book data
        book_data = {
            "title": "Sample Title",
            "author": "Sample Author",
            "year": 2022,
            "isbn": "1234567890",
        }
        # Create a BookBase instance using the sample book data
        book = BookBase(**book_data)
        # Assert that the attributes of the book object match the expected values
        self.assertEqual(book.title, "Sample Title")
        self.assertEqual(book.author, "Sample Author")
        self.assertEqual(book.year, 2022)
        self.assertEqual(book.isbn, "1234567890")

    def test_book_create(self):
        """
        Test case to verify the attributes of the BookCreate class.
        It creates a new instance of the BookCreate class using sample book data.
        """

        book_data = {
            "title": "Sample Title",
            "author": "Sample Author",
            "year": 2022,
            "isbn": "1234567890",
        }

        book_create = BookCreate(**book_data)

        self.assertEqual(book_create.title, "Sample Title")
        self.assertEqual(book_create.author, "Sample Author")
        self.assertEqual(book_create.year, 2022)
        self.assertEqual(book_create.isbn, "1234567890")

    def test_book_update(self):
        """
        Test case to verify the attributes of the BookUpdate class.
        It creates a new instance of the BookUpdate class using sample book data.
        """

        book_data = {
            "title": "Sample Title",
            "author": "Sample Author",
            "year": 2022,
            "isbn": "1234567890",
        }

        book_update = BookUpdate(**book_data)

        self.assertEqual(book_update.title, "Sample Title")
        self.assertEqual(book_update.author, "Sample Author")
        self.assertEqual(book_update.year, 2022)
        self.assertEqual(book_update.isbn, "1234567890")

    def test_book_in_db(self):
        """
        Test case to verify the attributes of the BookInDB class.
        It creates a new instance of the BookInDB class using sample book data.
        """

        book_data = {
            "id": 1,
            "title": "Sample Title",
            "author": "Sample Author",
            "year": 2022,
            "isbn": "1234567890",
        }

        book_in_db = BookInDB(**book_data)

        self.assertEqual(book_in_db.id, 1)
        self.assertEqual(book_in_db.title, "Sample Title")
        self.assertEqual(book_in_db.author, "Sample Author")
        self.assertEqual(book_in_db.year, 2022)
        self.assertEqual(book_in_db.isbn, "1234567890")


if __name__ == "__main__":
    unittest.main()
