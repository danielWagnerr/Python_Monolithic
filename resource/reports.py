import json
import os

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_report_user(user_id):
    user_id = str(user_id)
    value = None

    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)

    if user_id in json_db['users']:
        value = {'user': json_db['users'][user_id], 'books': []}
        if 'BooksLocations' in json_db['users'][user_id]:
            for bookId in json_db['users'][user_id]['BooksLocations']:
                if bookId in json_db['books']:
                    value['books'].append(json_db['books'][bookId])

    if value != None:
        return value
