import json

from resources import database

db = """{
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
            "FirstName": "Warren",
            "LastName": "Buffett",
            "Email": "WarrenBuffett@Email.com",
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


def setup_test_database() -> None:
    with open(database.get_database('database_test'), 'w',  encoding='utf-8') as f:
        json.dump(json.loads(db), f, ensure_ascii=False, indent=4)
