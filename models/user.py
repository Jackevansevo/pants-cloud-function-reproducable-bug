import datetime as dt

from sqlalchemy.orm import Mapped, mapped_column

from .db import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(128))
    age: Mapped[int]
    date_of_birth: Mapped[dt.date]
