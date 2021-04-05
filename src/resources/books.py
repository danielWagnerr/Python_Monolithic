import json

from src.resources.database import get_database


def get_books():
    database_path = get_database()

    with open(database_path, "r") as database:
        json_db = json.load(database)

    return json_db['books']


def get_book(book_id):
    database_path = get_database()

    with open(database_path, "r") as database:
        json_db = json.load(database)

    return json_db['books'].get(str(book_id))


def create_book(book: dict):
    if not book or not all(k in book for k in ("Name", "Authors", "Quantity")):
        return {"error": "Incorrect payload"}

    database_path = get_database()

    with open(database_path, "r") as database:
        json_db = json.load(database)

        last_id = json_db['lastBookId']
        book_id = last_id + 1

        json_db['books'][book_id] = book
        json_db['books'][book_id]['id'] = book_id
        json_db['lastBookId'] = book_id

    with open(database_path, "w") as database:
        json.dump(json_db, database, indent=4)

    return json_db['books'][book_id]


def update_book(book_id, book):
    database_path = get_database()

    value = None
    book_id = str(book_id)

    with open(database_path, "r") as database:
        json_db = json.load(database)

        if book_id in json_db['books']:
            for (key, val) in book.items():
                json_db['books'][book_id][key] = val

            value = json_db['books'][book_id]

            with open(database_path, "w") as write_database:
                json.dump(json_db, write_database, indent=4)

    return value


def delete_book(book_id):
    database_path = get_database()

    book_id = str(book_id)
    value = None

    with open(database_path, "r") as database:
        json_db = json.load(database)

        if book_id in json_db['books']:
            value = json_db['books'][book_id]
            del json_db['books'][book_id]

            with open(database_path, "w") as write_database:
                json.dump(json_db, write_database, indent=4)

    return value


def take_book(book_id, user_id):
    database_path = get_database()

    book_id = str(book_id)
    user_id = str(user_id)

    can_locate = False
    added_to_queue = False

    with open(database_path, "r") as database:
        json_db = json.load(database)

        can_take = (book_id in json_db['books']) and (user_id in json_db['users'])
        if can_take:
            users_locations = json_db['books'][book_id]['UsersLocations']
            quantity = json_db['books'][book_id]['Quantity']
            already_located = user_id in users_locations

            can_locate = quantity > len(users_locations) and not already_located

            if can_locate:
                json_db['books'][book_id]['UsersLocations'].append(user_id)
                json_db['users'][user_id]['BooksLocations'].append(book_id)

            already_in_queue = user_id in json_db['books'][book_id]['WaitingQueue']
            added_to_queue = not already_located and not can_locate and not already_in_queue

            if added_to_queue:
                json_db['books'][book_id]['WaitingQueue'].append(user_id)

    with open(database_path, "w") as database:
        json.dump(json_db, database, indent=4)

    return {
            'located': can_locate,
            'added_to_queue': added_to_queue
    } if can_take else None


def vacate_book(book_id, user_id):
    database_path = get_database()

    book_id = str(book_id)
    user_id = str(user_id)

    vacated = False

    with open(database_path, "r") as database:
        json_db = json.load(database)

        valid_ids = (book_id in json_db['books']) and (user_id in json_db['users'])
        if valid_ids:
            rented = user_id in json_db['books'][book_id]['UsersLocations']
            if rented:
                json_db['books'][book_id]['UsersLocations'].remove(user_id)
                json_db['users'][user_id]['BooksLocations'].remove(book_id)
                vacated = True

                waiting_queue = json_db['books'][book_id]['WaitingQueue']

                if waiting_queue:
                    first_in_line = waiting_queue.pop(0)
                    json_db['books'][book_id]['UsersLocations'].append(first_in_line)
                    json_db['users'][user_id]['BooksLocations'].append(book_id)

    with open(database_path, "w") as database:
        json.dump(json_db, database, indent=4)

    return {'vacated': vacated} if valid_ids else None
