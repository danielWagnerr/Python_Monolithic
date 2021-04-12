import json

from resources.database import get_database_path

database_path = get_database_path()


def get_users() -> dict:
    with open(database_path, "r") as database:
        json_db = json.load(database)

    return json_db['users']


def get_user(user_id: int) -> dict:
    with open(database_path, "r") as database:
        json_db = json.load(database)

    return json_db['users'].get(str(user_id))


def create_user(user: dict) -> dict:
    if not user or not all(k in user for k in ("FirstName", "LastName", "Email")):
        return {"error": "Incorrect payload"}

    with open(database_path, "r") as database:
        json_db = json.load(database)

        last_id = json_db['lastUserId']
        user_id = last_id + 1

        json_db['users'][user_id] = user
        json_db['users'][user_id]['id'] = user_id
        json_db['users'][user_id]['BooksLocations'] = []
        json_db['lastUserId'] = user_id

    with open(database_path, "w") as database:
        json.dump(json_db, database, indent=4)

    return json_db['users'][user_id]


def update_user(user_id: int, user: dict) -> dict:
    user_id = str(user_id)
    value = None

    with open(database_path, "r") as database:
        json_db = json.load(database)

        if user_id in json_db['users']:
            for(key, val) in user.items():
                json_db['users'][user_id][key] = val

            value = json_db['users'][user_id]

            with open(database_path, "w") as write_database:
                json.dump(json_db, write_database, indent=4)

    return value


def delete_user(user_id: int) -> dict:
    user_id = str(user_id)
    value = None

    with open(database_path, "r") as database:
        json_db = json.load(database)

        if user_id in json_db['users']:
            value = json_db['users'][user_id]
            del json_db['users'][user_id]

            with open(database_path, "w") as write_database:
                json.dump(json_db, write_database, indent=4)

    return value
