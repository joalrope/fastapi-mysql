from fastapi import FastAPI
from routes.user import user

server = FastAPI(
    title="CRUD with FastApi",
    description="Api to TC frontend",
    version="0.0.1",
    openapi_tags=[{
        "name": 'users',
        "description": "user routes"
    }],
)

server.include_router(user)
