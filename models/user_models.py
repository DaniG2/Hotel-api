from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str
    phone:str

class UserOut(BaseModel):
    username: str
    document: int
    tipoDocument: str
    email: str
    firstname: str
    lastName: str
    phone: str

class LogIn(BaseModel):
    username: str
    password: str