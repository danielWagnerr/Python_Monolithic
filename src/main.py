from flask import Flask, jsonify
from flask.globals import request
from resources import users, books

app = Flask(__name__)


def __response(body):
    status_code = 200 if 'error' not in body else 400
    return jsonify(body), status_code


@app.route("/", methods=['GET'])
def init():
    """
        Application start
    """
    return "Hello! The application is up, simulating a monolithic architecture."

# -----------------------------|
# REST Calls for Users Module.|
# -----------------------------|


@app.route("/users", methods=['GET'])
def get_users():
    """
        Return All Users list
    """

    response = users.get_users()
    return __response(response) if response else ('Not Found', 404)


@app.route("/users", methods=['POST'])
def user_create():
    """
        Create User
    """

    response = users.create_user(request.json)
    return __response(response) if response else ('Not Found', 404)


@app.route("/users/<user_id>", methods=['PUT'])
def user_update(user_id):
    """
        Update User
    """

    response = users.update_user(user_id, request.json)
    return __response(response) if response else ('Not Found', 404)


@app.route("/users/<user_id>", methods=['GET'])
def user_data(user_id):
    """
        Get User Data
    """
    response = users.get_user(user_id)
    return __response(response) if response else ('Not Found', 404)


@app.route("/users/<user_id>", methods=['DELETE'])
def user_delete(user_id):
    """
        Delete User
    """

    response = users.delete_user(user_id)
    return __response(response) if response else ('Not Found', 404)


# ---------------------------------|
# Rest Calls for Locations Module.|
# ---------------------------------|


@app.route("/books", methods=['GET'])
def get_books():
    """
        Return All Books list
    """

    response = books.get_books()
    return __response(response) if response else ('Not Found', 404)


@app.route("/books", methods=['POST'])
def book_create():
    """
        Create Book
    """

    response = books.create_book(request.json)
    return __response(response) if response else ('Not Found', 404)


@app.route("/books/<book_id>", methods=['PUT'])
def book_update(book_id):
    """
        Update Book
    """
    response = books.update_book(book_id, request.json)
    return __response(response) if response else ('Not Found', 404)


@app.route("/books/<book_id>", methods=['GET'])
def book_data(book_id):
    """
        Get Book Data
    """

    response = books.get_book(book_id)
    return __response(response) if response else ('Not Found', 404)


@app.route("/books/<book_id>", methods=['DELETE'])
def book_delete(book_id):
    """
        Delete Book
    """

    response = books.delete_book(book_id)
    return __response(response) if response else ('Not Found', 404)


@app.route("/books/take/<book_id>/<user_id>", methods=['POST'])
def book_take(book_id, user_id):
    """
        User takes a specific book
    """
    response = books.take_book(book_id, user_id)
    return __response(response) if response else ('Not Found', 404)


@app.route("/books/vacate/<book_id>/<user_id>", methods=['POST'])
def book_vacate(book_id, user_id):
    """
        User vacate a book
    """
    response = books.vacate_book(book_id, user_id)
    return __response(response) if response else ('Not Found', 404)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
