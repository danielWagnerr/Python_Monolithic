database = """{
    "lastUserId": 1,
    "lastBookId": 1,
    "users": {
        "0": {
            "FirstName": "James",
            "LastName": "Bond",
            "Email": "JamesBond@Email.com",
            "id": 0,
            "BooksLocations": [
                "0"
            ]
        },
        "1": {
            "FirstName": "Tester",
            "LastName": "Testador",
            "Email": "tester@Email.com",
            "id": 1,
            "BooksLocations": [
                "1"
            ]
        }
    },
    "books": {
        "0": {
            "Name": "Scrum",
            "Authors": [
                "Jeff Sutherland",
                "J. J. Sutherland"
            ],
            "Quantity": 8,
            "UsersLocations": [
                "0"
            ],
            "WaitingQueue": [],
            "id": 0
        },
        "1": {
            "Name": "Clean Code: A Handbook of Agile Software Craftsmanship",
            "Authors": [
                "Robert C. Martin",
                "Michael C. Feathers",
                "Timothy R. Ottinger"
            ],
            "Quantity": 5,
            "UsersLocations": [
                "1"
            ],
            "WaitingQueue": [],
            "id": 1
        }
    }
}"""


def get_mock_database() -> str:
    return database
