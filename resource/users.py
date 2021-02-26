import json
import os

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_users():
    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)

    if 'users' in json_db:
        return json_db['users']


def get_user(user_id):
    user_id = str(user_id)

    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)

    if 'users' in json_db:
        if user_id in json_db['users']:
            return json_db['users'][user_id]


def create_user(user):
    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'users' not in json_db:
            json_db['users'] = {}
        if 'lastUserId' not in json_db:
            json_db['lastUserId'] = -1
        
        lastid = json_db['lastUserId']
        
        json_db['users'][lastid+1] = user
        json_db['users'][lastid+1]['id'] = lastid+1
        json_db['lastUserId'] = lastid+1
        json.dump(json_db, database, indent=4)

    return json_db['users'][lastid+1]


def update_user(user_id, user):
    user_id = str(user_id)
    value = None

    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'users' not in json_db:
            json_db['users'] = {}
        if 'lastUserId' not in json_db:
            json_db['lastUserId'] = -1
        
        if user_id in json_db['users']:
            for(key, val) in user.items():
                json_db['users'][user_id][key] = val

            value = json_db['users'][user_id]
        
        json.dump(json_db, database, indent=4)

    if value != None:
        return value


def delete_user(user_id):
    user_id = str(user_id)
    value = None
    
    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'users' not in json_db:
            json_db['users'] = {}
        if 'lastUserId' not in json_db:
            json_db['lastUserId'] = -1
        
        if user_id in json_db['users']:
            value = json_db['users'][user_id]
            del json_db['users'][user_id]

        json.dump(json_db, database, indent=4)

    if value != None:
        return value
