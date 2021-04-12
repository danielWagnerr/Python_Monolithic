from unittest import TestCase, mock

from resources import books
from tests import mock_db


@mock.patch('builtins.open', new_callable=mock.mock_open, read_data=mock_db.get_mock_database())
class TestBooks(TestCase):
    def test_get_books(self, database_mock: mock.MagicMock) -> None:
        all_books = books.get_books()
        self.assertEqual(len(all_books), 2)

    def test_get_book(self, database_mock: mock.MagicMock) -> None:
        book = books.get_book(0)

        self.assertEqual(book['Name'], "Scrum")
        self.assertEqual(book['Authors'], [
                "Jeff Sutherland",
                "J. J. Sutherland"
        ])

    def test_create_book(self, database_mock: mock.MagicMock) -> None:
        book = books.create_book({
                "Name": "Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                "Authors": ["Martin Robert C."],
                "Quantity": 4
        })

        self.assertEqual(book['Name'], "Clean Architecture: A Craftsman's Guide to Software Structure and Design")
        self.assertEqual(book['Authors'], ["Martin Robert C."])
        self.assertEqual(book['Quantity'], 4)

    def test_update_book(self, database_mock: mock.MagicMock) -> None:
        book = books.update_book(1, {
                "Name": "Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                "Authors": ["Martin Robert C."],
                "Quantity": 10
        })

        self.assertEqual(book['Name'], "Clean Architecture: A Craftsman's Guide to Software Structure and Design")
        self.assertEqual(book['Authors'], ["Martin Robert C."])
        self.assertEqual(book['Quantity'], 10)

    def test_delete_book(self, database_mock: mock.MagicMock) -> None:
        book = books.delete_book(1)

        self.assertEqual(book['Name'], "Clean Code: A Handbook of Agile Software Craftsmanship")
        self.assertEqual(book['Authors'], ["Robert C. Martin", "Michael C. Feathers", "Timothy R. Ottinger"])
        self.assertEqual(book['Quantity'], 5)

    def test_take_book_success(self, database_mock: mock.MagicMock) -> None:
        response = books.take_book(1, 0)

        self.assertTrue(response['located'])
        self.assertFalse(response['added_to_queue'])

    def test_take_book_fail(self, database_mock: mock.MagicMock) -> None:
        response = books.take_book(1, 1)

        self.assertFalse(response['located'])
        self.assertFalse(response['added_to_queue'])

    def test_vacate_book_success(self, database_mock: mock.MagicMock) -> None:
        response = books.vacate_book(0, 0)

        self.assertTrue(response['vacated'])

    def test_vacate_book_fail(self, database_mock: mock.MagicMock) -> None:
        response = books.vacate_book(1, 0)

        self.assertFalse(response['vacated'])
