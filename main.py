from flask import Flask, jsonify
from flask.globals import request
from resource.users import create_user, update_user, delete_user, get_user, get_users
from resource.locations import get_books, get_book, create_book, update_book, delete_book, take_book, vacate_book

app = Flask(__name__)


@app.route("/", methods=['GET'])
def init():
    """
        Application start
    """
    return "Hello! The application is up, simulating a monolithic architecture."

# -----------------------------|
# Rest Calls for Users Module.|
# -----------------------------|


@app.route("/users", methods=['GET'])
def users():
    """
        Return All Users list
    """

    response = get_users()
    if response:
        return jsonify(response)

    return 'Not Found', 404


@app.route("/users", methods=['POST'])
def user_create():
    """
        Create User
    """

    response = create_user(request.json)
    if response:
        return jsonify(response)

    return 'Not Found', 404


@app.route("/users/<user_id>", methods=['PUT'])
def user_update(user_id):
    """
        Update User
    """

    response = update_user(user_id, request.json)
    if response:
        return jsonify(response)
    
    return 'Not Found', 404


@app.route("/users/<user_id>", methods=['GET'])
def user_data(user_id):
    """
        Get User Data
    """
    response = get_user(user_id)
    if response:
        return jsonify(response)
    
    return 'Not Found', 404


@app.route("/users/<user_id>", methods=['DELETE'])
def user_delete(user_id):
    """
        Delete User
    """

    response = delete_user(user_id)
    if response:
        return jsonify(response)
    
    return 'Not Found', 404

# ---------------------------------|
# Rest Calls for Locations Module.|
# ---------------------------------|


@app.route("/books", methods=['GET'])
def books():
    """
        Return All Books list
    """

    response = get_books()
    if response:
        return jsonify(response)
    
    return 'Not Found', 404


@app.route("/books", methods=['POST'])
def book_create():
    """
        Create Book
    """

    response = create_book(request.json)
    if response:
        return jsonify(response)
    
    return 'Not Found', 404


@app.route("/books/<book_id>", methods=['PUT'])
def book_update(book_id):
    """
        Update Book
    """
    response = update_book(book_id, request.json)
    if response:
        return jsonify(response)
    
    return 'Not Found', 404


@app.route("/books/<book_id>", methods=['GET'])
def book_data(book_id):
    """
        Get Book Data
    """

    response = get_book(book_id)
    if response:
        return jsonify(response)
    
    return 'Not Found', 404


@app.route("/books/<book_id>", methods=['DELETE'])
def book_delete(book_id):
    """
        Delete Book
    """

    response = delete_book(book_id)
    if response:
        return jsonify(response)
    
    return 'Not Found', 404


@app.route("/books/take/<book_id>/<user_id>", methods=['POST'])
def book_take(book_id, user_id):
    """
        User takes a specific book
    """
    response = take_book(book_id, user_id)
    if response:
        return jsonify(response)
    
    return 'Not Found', 404


@app.route("/books/vacate/<book_id>/<user_id>", methods=['POST'])
def book_vacate(book_id, user_id):
    """
        User vacate a book
    """
    response = vacate_book(book_id, user_id)
    if response:
        return jsonify(response)
    
    return 'Not Found', 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)
