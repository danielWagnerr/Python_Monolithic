from unittest import TestCase, mock

from src.resources import books, database
from src.tests import setup

database_path = database.get_database('database_test')


@mock.patch('src.resources.books.get_database', return_value=database_path)
class TestBooks(TestCase):
    """
    Os testes estão ordenados em ordem alfabética, pois estamos realizando operações no banco de dados
    e queremos manter o estado sem que um teste impacte em outro.
    A ordenação segue a seguinte regra:
        - Iniciar o nome do método com "test_" seguido de sua letra alfabética correspondente a ordem.
        - Por exemplo: "test_A_exemplo"
    """

    @classmethod
    def setUpClass(cls):
        setup.setup_test_database()

    def test_A_get_books(self, database_mock: mock.MagicMock) -> None:
        all_books = books.get_books()
        self.assertEqual(len(all_books), 2)

    def test_B_get_book(self, database_mock: mock.MagicMock) -> None:
        book = books.get_book(0)

        self.assertEqual(book['Name'], "Scrum")
        self.assertEqual(book['Authors'], [
                "Jeff Sutherland",
                "J. J. Sutherland"
        ])

    def test_C_create_book(self, database_mock: mock.MagicMock) -> None:
        book = books.create_book({
                "Name": "Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                "Authors": ["Martin Robert C."],
                "Quantity": 4
        })

        self.assertEqual(book['Name'], "Clean Architecture: A Craftsman's Guide to Software Structure and Design")
        self.assertEqual(book['Authors'], ["Martin Robert C."])
        self.assertEqual(book['Quantity'], 4)

    def test_D_update_book(self, database_mock: mock.MagicMock) -> None:
        book = books.update_book(2, {
                "Name": "Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                "Authors": ["Martin Robert C."],
                "Quantity": 10
        })

        self.assertEqual(book['Name'], "Clean Architecture: A Craftsman's Guide to Software Structure and Design")
        self.assertEqual(book['Authors'], ["Martin Robert C."])
        self.assertEqual(book['Quantity'], 10)

    def test_E_delete_book(self, database_mock: mock.MagicMock) -> None:
        book = books.delete_book(2)

        self.assertEqual(book['Name'], "Clean Architecture: A Craftsman's Guide to Software Structure and Design")
        self.assertEqual(book['Authors'], ["Martin Robert C."])
        self.assertEqual(book['Quantity'], 10)

    def test_F_take_book_success(self, database_mock: mock.MagicMock) -> None:
        response = books.take_book(1, 0)

        self.assertTrue(response['located'])
        self.assertFalse(response['added_to_queue'])

    def test_G_take_book_fail(self, database_mock: mock.MagicMock) -> None:
        response = books.take_book(1, 1)

        self.assertFalse(response['located'])
        self.assertFalse(response['added_to_queue'])

    def test_H_vacate_book_success(self, database_mock: mock.MagicMock) -> None:
        response = books.vacate_book(1, 0)

        self.assertTrue(response['vacated'])

    def test_F_take_book_fail(self, database_mock: mock.MagicMock) -> None:
        response = books.vacate_book(1, 0)

        self.assertFalse(response['vacated'])
