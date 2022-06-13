from click import password_option
from fastapi import APIRouter
from cryptography.fernet import Fernet
from config.db import conn
from models.user import users
from schemas.user import User, ApiResp

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()


@user.get('/users', response_model=list[User], tags=['users'])
def find_all_user():
    return conn.execute(users.select()).fetchall()


@user.post('/users', response_model=User, tags=['users'])
def create_user(user: User):
    password = f.encrypt(user.password.encode("utf-8"))
    new_user = {"name": user.name,
                "email": user.email,
                "password": password}

    result = conn.execute(users.insert().values(new_user))

    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get('/users/{id}', response_model=User, tags=['users'])
def find_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


""" @user.put('/users/update-password/{id}', tags=['users'])
def update_user_password(id: str, user: User):
    conn.execute(users.update()
                 .values(password=user.password)
                 .where(users.c.id == id))

    return {f"message": 'update user {id}'} """


@user.put('/users/{id}', tags=['users'])
def update_user(id: str, user: User):
    conn.execute(users.update()
                 .values(password=user.password)
                 .where(users.c.id == id))

    return {f"message": 'update user {id}'}


@user.delete('/users/{id}', response_model=ApiResp, tags=['users'])
def delete_user(id: str):
    deleted_user = conn.execute(users.select()
                                .where(users.c.id == id)).first()

    conn.execute(users.delete().where(users.c.id == id))

    return {
        "ok": True,
        "msg": f"user with id: {id} was deleted",
        "result": deleted_user
    }
