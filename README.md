# Python_Monolithic
 A proof of concept of a monolithic architecture written in python and using flask and json.
 Simulate a simple library system.
 
Has a simple automatic id system creation.

Architecture based Example (not equals, just simulates the interactions and comunication workflow):

![monolithic](https://raw.githubusercontent.com/LucasGab/Python_Monolithic/master/monolithic.png)

# Instruction

1. Clone the repository.
2. Needs Python 3.* .
3. Initiate a new `virtualenv venv` and install the `requirements.txt`.
4. Run the main.py and use a tool like postman to make the requests.

# End Points

    GET / : Welcome Message
        body: Nothing
    
    Users Module:

    GET /users : Return All Users list
        body: Nothing
    POST /users : Create User
        body:
        {
            "FirstName": "James",
            "LastName": "Bond",
            "Email":"JamesBond@Email.com"
        }

    PUT /users/<user_id> : Update User
        body:
        {
            "FirstName": "James",
            "LastName": "Bondeee",
            "Email":"JamesBond@Email.com"
        }

    GET /users/<user_id> : Get User Data
        body: Nothing
    DELETE /users/<user_id> : Delete User,
        body: Nothing

    Books Module:

    GET /books : Return All Books list
        body: Nothing
    POST /books : Create Book
        body:
        {
            "Name":"Scrum",
            "Authors":["Jeff Sutherland","J. J. Sutherland"],
            "Quantity": 10
        }

    PUT /books/<book_id> : Update Book
        body:
        {
            "Name":"Scrum",
            "Authors":["Jeff Sutherland","J. J. Sutherland"],
            "Quantity": 5
        }

    GET /books/<book_id> : Get Book Data
        body: Nothing
    DELETE /books/<book_id> : Delete Book
        body: Nothing
    POST /books/take/<book_id>/<user_id>: User takes a specific book
        body: Nothing
    POST /books/vacate/<book_id>/<user_id>: User vacate a book
        body: Nothing

    Reports Module:
    
    GET reports/<user_id> : Get User Report
        body: Nothing
