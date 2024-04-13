import datetime as dt
import random
from uuid import uuid4

from flask import Blueprint, request
from sqlalchemy import select

from models.user import User, db

views = Blueprint("views", __name__, url_prefix="/")


@views.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        user = User(
            name=str(uuid4()),
            age=random.randrange(1, 100),
            date_of_birth=dt.date(random.randrange(1960, 2024), 1, 1),
        )
        db.session.add(user)
        db.session.commit()
        return {
            "user": {
                "id": user.id,
                "name": user.name,
                "date_of_birth": user.date_of_birth,
            }
        }
    else:
        users = db.session.scalars(select(User)).all()
        return [
            {
                "id": user.id,
                "name": user.name,
                "date_of_birth": user.date_of_birth,
            }
            for user in users
        ]
