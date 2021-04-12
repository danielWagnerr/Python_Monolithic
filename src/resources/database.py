import os


def get_database_path(db: str = 'database') -> str:
    database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return f'{database_path}/database/{db}.json'
