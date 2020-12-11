from db.user_db import UserInDB
from db.user_db import update_user, get_user
from models.user_models import UserIn, UserOut

import datetime
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

api = FastAPI()

@api.get("/user/perfil/{username}")
async def get_phone(username: str):

    user_in_db = get_user(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = UserOut(**user_in_db.dict())

    return  user_out


@api.put("/user/perfil/")
async def make_user(user_in: UserIn):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    if user_in_db.password == user_in.password:
        user_in_db.phone = user_in.phone
        user_in_db = update_user(user_in_db)
        user_out = UserOut(**user_in_db.dict())
        return  user_out
    
    return "Contraseña incorrecta" 