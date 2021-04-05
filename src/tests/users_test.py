from unittest import TestCase, mock

from src.resources import users, database
from src.tests import setup

database_path = database.get_database('database_test')


@mock.patch('src.resources.users.get_database', return_value=database_path)
class TestUsers(TestCase):
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

    def test_A_get_users(self, database_mock: mock.MagicMock) -> None:
        all_users = users.get_users()
        self.assertEqual(len(all_users), 2)

    def test_B_get_user(self, database_mock: mock.MagicMock) -> None:
        user = users.get_user(0)
        self.assertEqual(user['FirstName'], 'James')
        self.assertEqual(user['Email'], 'JamesBond@Email.com')
        self.assertEqual(user['id'], 0)

    def test_C_create_user(self, database_mock: mock.MagicMock) -> None:
        created_user = users.create_user({
            "FirstName": "Daniel",
            "LastName": "Tester",
            "Email": "daniel@test.com"
        })

        self.assertEqual(created_user['FirstName'], 'Daniel')
        self.assertEqual(created_user['LastName'], 'Tester')
        self.assertEqual(created_user['Email'], 'daniel@test.com')

    def test_D_update_user(self, database_mock: mock.MagicMock) -> None:
        user = {
            "FirstName": "Dan",
            "LastName": "Wagner",
            "Email": "daniel@tester.com"
        }

        created_user = users.update_user(2, user)

        self.assertEqual(created_user['FirstName'], 'Dan')
        self.assertEqual(created_user['LastName'], 'Wagner')
        self.assertEqual(created_user['Email'], 'daniel@tester.com')

    def test_E_delete_user(self, database_mock: mock.MagicMock) -> None:
        created_user = users.delete_user(2)

        self.assertEqual(created_user['FirstName'], 'Dan')
        self.assertEqual(created_user['LastName'], 'Wagner')
        self.assertEqual(created_user['Email'], 'daniel@tester.com')
