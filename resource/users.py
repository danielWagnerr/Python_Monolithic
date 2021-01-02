import json
import os

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def getUsers():
    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)

    if 'users' in jsonDB:
        return jsonDB['users']

def getUser(user_id):
    user_id = str(user_id)

    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)

    if 'users' in jsonDB:
        if user_id in jsonDB['users']:
            return jsonDB['users'][user_id]

def createUser(user):
    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'users' not in jsonDB:
            jsonDB['users'] = {}
        if 'lastUserId' not in jsonDB:
            jsonDB['lastUserId'] = -1
        
        lastid = jsonDB['lastUserId']
        
        jsonDB['users'][lastid+1] = user
        jsonDB['users'][lastid+1]['id'] = lastid+1
        jsonDB['lastUserId'] = lastid+1
        json.dump(jsonDB,database,indent=4)

    return jsonDB['users'][lastid+1]

def updateUser(user_id,user):
    user_id = str(user_id)
    value = None

    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'users' not in jsonDB:
            jsonDB['users'] = {}
        if 'lastUserId' not in jsonDB:
            jsonDB['lastUserId'] = -1
        
        if user_id in jsonDB['users']:
            value = {}
            
            for(key,val) in user.items(): 
                jsonDB['users'][user_id][key] = val

            value = jsonDB['users'][user_id]
        
        json.dump(jsonDB,database,indent=4)

    if (value != None):
        return value

def deleteUser(user_id):
    user_id = str(user_id)
    value = None
    
    with open('{}/database/database.json'.format(database_path), "r") as database:
        jsonDB = json.load(database)
    with open('{}/database/database.json'.format(database_path), "w") as database:
        if 'users' not in jsonDB:
            jsonDB['users'] = {}
        if 'lastUserId' not in jsonDB:
            jsonDB['lastUserId'] = -1
        
        if user_id in jsonDB['users']:
            value={}
            value = jsonDB['users'][user_id]
            del jsonDB['users'][user_id]

        json.dump(jsonDB,database,indent=4)

    if(value != None):
        return value

if __name__ == '__main__':
    '''
    user = {
        "FirstName": "James",
        "LastName": "Bond",
        "Email":"JamesBond@Email.com"
    }
    user2 = {
        "FirstName": "Warren",
        "LastName": "Buffett",
        "Email":"WarrenBuffett@Email.com"
    }
    '''
    pass
