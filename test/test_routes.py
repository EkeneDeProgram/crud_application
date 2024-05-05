import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from fastapi import HTTPException
from unittest.mock import MagicMock
from app.routes import read_books, read_book, create_book, update_book, delete_book
from app.models import Book
from app.schemas import BookInDB, BookCreate, BookUpdate


class TestBookRoutes(unittest.TestCase):

    def test_read_books(self):
        """
        Test case to verify the behavior of the read_books route.
        It mocks the database session to return sample books and then calls
        the route function with the mocked session.
        """
        # Mock the database session
        fake_db_session = MagicMock()
        # Mock the query method to return sample books
        sample_books = [
            Book(id=1, title="Book 1", author="Author 1", year=2022, isbn="1234567890"),
            Book(id=2, title="Book 2", author="Author 2", year=2023, isbn="2345678901"),
        ]
        fake_db_session.query.return_value.all.return_value = sample_books

        # Call the route function with the mocked session
        response = read_books(db=fake_db_session)

        # Assert the response
        expected_response = [
            BookInDB(
                id=book.id,
                title=book.title,
                author=book.author,
                year=book.year,
                isbn=book.isbn,
            )
            for book in sample_books
        ]
        self.assertEqual(response, expected_response)

    def test_read_book_valid_id(self):
        """
        Test case to verify the behavior of the read_book route with a valid book ID.
        It mocks the database session and sets up a mock query object to simulate
        querying a book with the specified ID.
        """
        # Mock the database session
        fake_db_session = MagicMock()

        # Define book_id
        book_id = "1"

        # Mock the query method to return a mock query object
        query_mock = MagicMock()

        # Mock the filter and first methods of the query object
        filter_mock = MagicMock()

        # Define mock_orm_book based on your previous setup
        mock_orm_book = MagicMock()
        mock_orm_book.id = 1
        mock_orm_book.title = "Sample Book 1"
        mock_orm_book.author = "Author 1"
        mock_orm_book.year = 2022
        mock_orm_book.isbn = "1234567890"

        # Set the return value of the first method to the mock_orm_book
        filter_mock.first.return_value = mock_orm_book

        # Attach the filter mock to the query mock
        query_mock.filter.return_value = filter_mock

        # Set the return value of the query method to the query mock
        fake_db_session.query.return_value = query_mock

        # Call the route function with the mocked session
        response = read_book(book_id, db=fake_db_session)

        # Assert the response
        expected_response = BookInDB(
            id=mock_orm_book.id,
            title=mock_orm_book.title,
            author=mock_orm_book.author,
            year=mock_orm_book.year,
            isbn=mock_orm_book.isbn,
        )
        self.assertEqual(response, expected_response)

    def test_read_book_invalid_id(self):
        """
        Test case to verify the behavior of the read_book route with an invalid book ID.
        It mocks the database session and attempts to read a book with an invalid ID.
        it's expected to raise an HTTPException with status code 422 (Unprocessable Entity).
        """
        # Mock the database session
        fake_db_session = MagicMock()

        # Define invalid book_id
        invalid_book_id = "invalid_id"

        # Call the route function with the mocked session and invalid book ID
        with self.assertRaises(HTTPException) as context:
            read_book(invalid_book_id, db=fake_db_session)

        # Check if the expected HTTPException is raised
        self.assertEqual(context.exception.status_code, 422)

    def test_create_book(self):
        """
        Test case to verify the behavior of the create_book route.
        It mocks the database session and creates a new book using sample book data.
        """
        # Mock the database session
        fake_db_session = MagicMock()

        # Define a sample book data to create
        sample_book_data = {
            "title": "New Book",
            "author": "New Author",
            "year": 2023,
            "isbn": "9876543210",
        }

        # Define the expected created book object
        expected_created_book = Book(
            id=1, **sample_book_data  # Assuming this is the ID assigned by the database
        )

        # Mock the add, commit, and refresh methods of the session
        fake_db_session.add.return_value = None
        fake_db_session.commit.return_value = None
        fake_db_session.refresh.return_value = None

        # Mock the behavior of the database to return an object with ID after insertion
        fake_db_session.add.side_effect = lambda instance: setattr(instance, "id", 1)

        # Call the route function with the mocked session and sample book data
        response = create_book(BookCreate(**sample_book_data), db=fake_db_session)

        # Assert that the book object returned has the same attributes as the expected created book
        self.assertEqual(response.id, expected_created_book.id)
        self.assertEqual(response.title, expected_created_book.title)
        self.assertEqual(response.author, expected_created_book.author)
        self.assertEqual(response.year, expected_created_book.year)
        self.assertEqual(response.isbn, expected_created_book.isbn)

    def test_update_book(self):
        """
        Test case to verify the behavior of the update_book route.
        It mocks the database session and updates an existing book with sample update data.
        """
        # Mock the database session
        fake_db_session = MagicMock()

        # Define the book ID to update
        book_id = 1

        # Define a sample book update data
        update_data = {
            "title": "Updated Title",
            "author": "Updated Author",
            "year": 2024,
            "isbn": "9876543210",
        }

        # Mock the query method to return the existing book object
        existing_book = Book(
            id=book_id,
            title="Existing Title",
            author="Existing Author",
            year=2023,
            isbn="1234567890",
        )
        fake_db_session.query().filter().first.return_value = existing_book

        # Call the route function with the mocked session and update data
        response = update_book(book_id, BookUpdate(**update_data), db=fake_db_session)

        # Assert that the book object returned has the updated attributes
        self.assertEqual(response.id, book_id)
        self.assertEqual(response.title, update_data["title"])
        self.assertEqual(response.author, update_data["author"])
        self.assertEqual(response.year, update_data["year"])
        self.assertEqual(response.isbn, update_data["isbn"])

    def test_delete_book(self):
        """
        Test case to verify the behavior of the delete_book route.
        It mocks the database session and deletes an existing book with the specified ID.
        """
        # Mock the database session
        fake_db_session = MagicMock()

        # Define the book ID to delete
        book_id = 1

        # Mock the query method to return the existing book object
        existing_book = Book(
            id=book_id,
            title="Existing Title",
            author="Existing Author",
            year=2023,
            isbn="1234567890",
        )
        fake_db_session.query().filter().first.return_value = existing_book

        # Call the route function with the mocked session
        response = delete_book(book_id, db=fake_db_session)

        # Assert that the book object returned is the one deleted
        self.assertEqual(response.id, book_id)

        # Assert that the delete method of the session was called with the correct book object
        fake_db_session.delete.assert_called_once_with(existing_book)

        # Assert that the commit method of the session was called
        fake_db_session.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
