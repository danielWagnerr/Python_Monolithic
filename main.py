from flask import Flask, jsonify, make_response
from flask.globals import request
from resource.users import createUser,updateUser, deleteUser, getUser, getUsers
from resource.reports import getReportUser
from resource.locations import getBooks,getBook,createBook,updateBook,deleteBook,takeBook,vacateBook

app = Flask(__name__)

@app.route("/", methods=['GET'])
def init():
    ''' Application start '''
    return "Hello! The application is up, simulating a monolithic architecture."

#-----------------------------|
# Rest Calls for Users Module.|
#-----------------------------|

@app.route("/users", methods=['GET'])
def users():
    ''' Return All Users list '''
    response = getUsers()
    if response:
        return jsonify(response)
    
    return 'Error',404

@app.route("/users", methods=['POST'])
def user_create():
    ''' Create User '''
    response = createUser(request.json)
    if response:
        return jsonify(response)
    
    return 'Error',404

@app.route("/users/<user_id>", methods=['PUT'])
def user_update(user_id):
    ''' Create User '''
    response = updateUser(user_id,request.json)
    if response:
        return jsonify(response)
    
    return 'Error',404

@app.route("/users/<user_id>", methods=['GET'])
def user_data(user_id):
    ''' Get User Data'''
    response = getUser(user_id)
    if response:
        return jsonify(response)
    
    return 'Error',404

@app.route("/users/<user_id>", methods=['DELETE'])
def user_delete(user_id):
    ''' Delete User '''
    response = deleteUser(user_id)
    if response:
        return jsonify(response)
    
    return 'Error',404

#---------------------------------|
# Rest Calls for Locations Module.|
#---------------------------------|

@app.route("/books", methods=['GET'])
def books():
    ''' Return All Books list '''
    response = getBooks()
    if response:
        return jsonify(response)
    
    return 'Error',404

@app.route("/books", methods=['POST'])
def book_create():
    ''' Create Book '''
    response = createBook(request.json)
    if response:
        return jsonify(response)
    
    return 'Error',404

@app.route("/books/<book_id>", methods=['PUT'])
def book_update(book_id):
    ''' Update Book '''
    response = updateBook(book_id,request.json)
    if response:
        return jsonify(response)
    
    return 'Error',404

@app.route("/books/<book_id>", methods=['GET'])
def book_data(book_id):
    ''' Get Book Data'''
    response = getBook(book_id)
    if response:
        return jsonify(response)
    
    return 'Error',404

@app.route("/books/<book_id>", methods=['DELETE'])
def book_delete(book_id):
    ''' Delete Book '''
    response = deleteBook(book_id)
    if response:
        return jsonify(response)
    
    return 'Error',404

@app.route("/books/<book_id>/<user_id>", methods=['POST'])
def book_take(book_id,user_id):
    ''' Delete Book '''
    response = takeBook(book_id,user_id)
    if response:
        return jsonify(response)
    
    return 'Error',404

@app.route("/books/<book_id>/<user_id>", methods=['POST'])
def book_vacate(book_id,user_id):
    ''' Delete Book '''
    response = vacateBook(book_id,user_id)
    if response:
        return jsonify(response)
    
    return 'Error',404
#-------------------------------|
# Rest Calls for Reports Module.|
#---------------------------------|

@app.route("/<user_id>/reports", methods=['GET'])
def report_user(user_id):
    ''' Return All Books list '''
    response = getReportUser(user_id)
    if response:
        return jsonify(response)
    
    return 'Error',404

if __name__ == '__main__':
    app.run(port=5000,debug=True)

