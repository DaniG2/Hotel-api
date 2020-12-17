from datetime import time
from typing import  Dict
from pydantic import BaseModel
#from pydantic.types import StrIntFloat

class UserInDB(BaseModel):
    username: str
    password: str
    document: int
    tipoDocument: str
    email: str
    firstname: str
    lastName: str
    phone: str

database_users = Dict[str, UserInDB]
database_users = {
    "jonier1": UserInDB(**{"username":"jonier1",
                            "password":"cuatros",
                            "document":1234,
                            "tipoDocument": "CC",
                            "email":"joni@hotmail.com",
                            "firstname":"jonier",
                            "lastName":"escobar",
                            "phone": "111"}),              

    "martin2": UserInDB(**{"username":"martin2",
                            "password":"guitarras",
                            "document":12345,
                            "tipoDocument": "CC",
                            "email":"mart@hotmail.com",
                            "firstname":"martin",
                            "lastName":"bocarejo",
                            "phone": "222"}),

    "george3": UserInDB(**{"username":"george3",
                            "password":"bandolas",
                            "document":123456,
                            "tipoDocument": "CC",
                            "email":"geog@hotmail.com",
                            "firstname":"george",
                            "lastName":"conde",
                            "phone": "333"}),

    "juan4": UserInDB(**{"username":"juan4",
                            "password":"maracas",
                            "document":1234567,
                            "tipoDocument": "CC",
                            "email":"juan@hotmail.com",
                            "firstname":"juan",
                            "lastName":"cervera",
                            "phone": "444"}),
    
    "daniela5": UserInDB(**{"username":"daniela5",
                            "password":"tiples",
                            "document":12345678,
                            "tipoDocument": "CC",
                            "email":"dani@hotmail.com",
                            "firstname":"daniela",
                            "lastName":"garcía",
                            "phone": "555"})
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db

def post_user(username:str):
    if username in database_users.keys():
        return database_users[username].password
    else:
        return None