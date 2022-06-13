from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str]
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]


class ApiResp(BaseModel):
    ok: bool
    msg: str
    result: list
