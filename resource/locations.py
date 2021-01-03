import json
import os

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def getBooks():
    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)

    if 'books' in jsonDB:
        return jsonDB['books']
       
def getBook(book_id):
    book_id = str(book_id)
    
    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)

    if 'books' in jsonDB:
        if book_id in jsonDB['books']:
            return jsonDB['books'][book_id]

def createBook(book):
    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'books' not in jsonDB:
            jsonDB['books'] = {}
        if 'lastBookId' not in jsonDB:
            jsonDB['lastBookId'] = -1
        
        lastid = jsonDB['lastBookId']
        
        jsonDB['books'][lastid+1] = book
        jsonDB['books'][lastid+1]['id'] = lastid+1
        jsonDB['lastBookId'] = lastid+1
        json.dump(jsonDB,database,indent=4)

    return jsonDB['books'][lastid+1]

def updateBook(book_id,book):
    value = None

    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'books' not in jsonDB:
            jsonDB['books'] = {}
        if 'lastBookId' not in jsonDB:
            jsonDB['lastBookId'] = -1
        
        if book_id in jsonDB['books']:
            value = {}
            
            for(key,val) in book.items(): 
                jsonDB['books'][book_id][key] = val
    
            value = jsonDB['books'][book_id]
            json.dump(jsonDB,database,indent=4)

    if(value != None):
        return value

def deleteBook(book_id):
    book_id = str(book_id)
    value = None

    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'books' not in jsonDB:
            jsonDB['books'] = {}
        if 'lastBookId' not in jsonDB:
            jsonDB['lastBookId'] = -1
        
        if book_id in jsonDB['books']:
            value={}
            value = jsonDB['books'][book_id]
            del jsonDB['books'][book_id]

        json.dump(jsonDB,database,indent=4)

    if(value != None):
        return value

def takeBook(book_id,user_id):
    value = None
    book_id = str(book_id)
    user_id = str(user_id)

    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'books' not in jsonDB:
            jsonDB['books'] = {}
        if 'lastBookId' not in jsonDB:
            jsonDB['lastBookId'] = -1
        
        if (book_id in jsonDB['books']) and (user_id in jsonDB['users']):
            if "UsersLocations" not in jsonDB['books'][book_id]:
                jsonDB['books'][book_id]['UsersLocations'] = []
            if "BooksLocations" not in jsonDB['users'][user_id]:
                jsonDB['users'][user_id]['BooksLocations'] = []
            
            jsonDB['books'][book_id]['UsersLocations'].append(user_id)
            jsonDB['users'][user_id]['BooksLocations'].append(book_id)

            value = jsonDB['books'][book_id]['UsersLocations']

        json.dump(jsonDB,database,indent=4)

    if(value != None):
        return value

def vacateBook(book_id,user_id):
    value = None
    book_id = str(book_id)
    user_id = str(user_id)

    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'books' not in jsonDB:
            jsonDB['books'] = {}
        if 'lastBookId' not in jsonDB:
            jsonDB['lastBookId'] = -1
        
        if (book_id in jsonDB['books']) and (user_id in jsonDB['users']):
            if (("UsersLocations" in jsonDB['books'][book_id]) 
            and ("BooksLocations" in jsonDB['users'][user_id])):
                if(user_id in jsonDB['books'][book_id]['UsersLocations']):
                    jsonDB['books'][book_id]['UsersLocations'].remove(user_id)
                    jsonDB['users'][user_id]['BooksLocations'].remove(book_id)
                    value = jsonDB['books'][book_id]['UsersLocations']

        json.dump(jsonDB,database,indent=4)

    if(value != None):
        return value

if __name__ == '__main__':
    '''
    book = {
        "Name":"Scrum",
        "Authors":["Jeff Sutherland","J. J. Sutherland"],
        "Quantity": 10
    }
    book2 = {
        "Name":"Clean Code: A Handbook of Agile Software Craftsmanship",
        "Authors":["Robert C. Martin","Michael C. Feathers","Timothy R. Ottinger"],
        "Quantity": 5
    }
    '''
    pass
