import json
import os

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def getReportUser(user_id):
    user_id = str(user_id)
    value = None

    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)

    if user_id in jsonDB['users']:
        value = {}
        value['user'] = jsonDB['users'][user_id]
        value['books'] = []
        if 'BooksLocations' in jsonDB['users'][user_id]:
            for bookId in jsonDB['users'][user_id]['BooksLocations']:
                if bookId in jsonDB['books']:
                    value['books'].append(jsonDB['books'][bookId])

    if(value != None):
        return value

if __name__ == '__main__':
    pass
