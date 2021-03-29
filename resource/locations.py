import json
import os

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_books():
    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)

    if 'books' in json_db:
        return json_db['books']


def get_book(book_id):
    book_id = str(book_id)

    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)

    if 'books' in json_db:
        if book_id in json_db['books']:
            return json_db['books'][book_id]


def create_book(book):
    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'books' not in json_db:
            json_db['books'] = {}
        if 'lastBookId' not in json_db:
            json_db['lastBookId'] = -1

        lastid = json_db['lastBookId']

        json_db['books'][lastid + 1] = book
        json_db['books'][lastid + 1]['id'] = lastid + 1
        json_db['lastBookId'] = lastid + 1
        json.dump(json_db, database, indent=4)

    return json_db['books'][lastid + 1]


def update_book(book_id, book):
    value = None

    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'books' not in json_db:
            json_db['books'] = {}
        if 'lastBookId' not in json_db:
            json_db['lastBookId'] = -1

        if book_id in json_db['books']:
            for (key, val) in book.items():
                json_db['books'][book_id][key] = val

            value = json_db['books'][book_id]
            json.dump(json_db, database, indent=4)

    if value != None:
        return value


def delete_book(book_id):
    book_id = str(book_id)
    value = None

    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'books' not in json_db:
            json_db['books'] = {}
        if 'lastBookId' not in json_db:
            json_db['lastBookId'] = -1

        if book_id in json_db['books']:
            value = json_db['books'][book_id]
            del json_db['books'][book_id]

        json.dump(json_db, database, indent=4)

    if value != None:
        return value


def take_book(book_id, user_id):
    book_id = str(book_id)
    user_id = str(user_id)

    can_locate = False
    added_to_queue = False

    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'books' not in json_db:
            json_db['books'] = {}
        if 'lastBookId' not in json_db:
            json_db['lastBookId'] = -1

        can_take = (book_id in json_db['books']) and (user_id in json_db['users'])
        if can_take:
            if "UsersLocations" not in json_db['books'][book_id]:
                json_db['books'][book_id]['UsersLocations'] = []
            if "BooksLocations" not in json_db['users'][user_id]:
                json_db['users'][user_id]['BooksLocations'] = []

            users_locations = json_db['books'][book_id]['UsersLocations']
            quantity = json_db['books'][book_id]['Quantity']
            not_already_located = user_id not in users_locations

            can_locate = quantity > len(users_locations) and not_already_located

            if can_locate:
                json_db['books'][book_id]['UsersLocations'].append(user_id)
                json_db['users'][user_id]['BooksLocations'].append(book_id)

            not_already_in_queue = user_id not in json_db['books'][book_id]['WaitingQueue']
            added_to_queue = not_already_located and not can_locate and not_already_in_queue

            if added_to_queue:
                json_db['books'][book_id]['WaitingQueue'].append(user_id)

        json.dump(json_db, database, indent=4)

    return {
            'located': can_locate,
            'added_to_queue': added_to_queue
    } if can_take else None


def vacate_book(book_id, user_id):
    book_id = str(book_id)
    user_id = str(user_id)

    vacated = False
    took = False

    with open('{}/database/database.json'.format(database_path), "r") as database:
        json_db = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'books' not in json_db:
            json_db['books'] = {}
        if 'lastBookId' not in json_db:
            json_db['lastBookId'] = -1

        if (book_id in json_db['books']) and (user_id in json_db['users']):
            took = ("UsersLocations" in json_db['books'][book_id]) and ("BooksLocations" in json_db['users'][user_id])
            if took:
                if user_id in json_db['books'][book_id]['UsersLocations']:
                    json_db['books'][book_id]['UsersLocations'].remove(user_id)
                    json_db['users'][user_id]['BooksLocations'].remove(book_id)
                    vacated = True

                waiting_queue = json_db['books'][book_id]['WaitingQueue']
                if waiting_queue:
                    first_in_line = waiting_queue.pop(0)

                    json_db['books'][book_id]['UsersLocations'].append(first_in_line)
                    json_db['users'][user_id]['BooksLocations'].append(book_id)

        json.dump(json_db, database, indent=4)

    return {'vacated': vacated} if took else None
