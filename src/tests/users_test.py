from unittest import TestCase, mock

from resources import users
from tests import mock_db


@mock.patch('builtins.open', new_callable=mock.mock_open, read_data=mock_db.get_mock_database())
class TestUsers(TestCase):
    def test_get_users(self, database_mock: mock.MagicMock) -> None:
        all_users = users.get_users()
        self.assertEqual(len(all_users), 2)

    def test_get_user(self, database_mock: mock.MagicMock) -> None:
        user = users.get_user(0)
        self.assertEqual(user['FirstName'], 'James')
        self.assertEqual(user['Email'], 'JamesBond@Email.com')
        self.assertEqual(user['id'], 0)

    def test_create_user(self, database_mock: mock.MagicMock) -> None:
        created_user = users.create_user({
            "FirstName": "Daniel",
            "LastName": "Tester",
            "Email": "daniel@test.com"
        })

        self.assertEqual(created_user['FirstName'], 'Daniel')
        self.assertEqual(created_user['LastName'], 'Tester')
        self.assertEqual(created_user['Email'], 'daniel@test.com')

    def test_update_user(self, database_mock: mock.MagicMock) -> None:
        user = {
            "FirstName": "Dan",
            "LastName": "Wagner",
            "Email": "daniel@tester.com"
        }

        created_user = users.update_user(1, user)

        self.assertEqual(created_user['FirstName'], 'Dan')
        self.assertEqual(created_user['LastName'], 'Wagner')
        self.assertEqual(created_user['Email'], 'daniel@tester.com')

    def test_delete_user(self, database_mock: mock.MagicMock) -> None:
        created_user = users.delete_user(1)

        self.assertEqual(created_user['FirstName'], 'Tester')
        self.assertEqual(created_user['LastName'], 'Testador')
        self.assertEqual(created_user['Email'], 'tester@Email.com')
