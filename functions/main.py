import os

import functions_framework
from sqlalchemy import URL, create_engine, select
from sqlalchemy.orm import Session

from models.user import User

url_object = URL.create(
    "postgresql+psycopg",
    username="postgres",
    password=os.environ.get("DB_PASSWORD", "postgres"),
    host=os.environ.get("DB_HOST", "localhost"),
    database=os.environ.get("DB_NAME", "example"),
    port=os.environ.get("DB_PORT", 5432),
)

engine = create_engine(url_object)

@functions_framework.http
def handler(request):
    with Session(engine) as session:
        users = session.scalars(select(User)).all()
        return [
            {
                "id": user.id,
                "name": user.name,
                "date_of_birth": user.date_of_birth,
            }
            for user in users
        ]

    return "hello world"
