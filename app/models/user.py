import hashlib
import re
from contextlib import suppress
from datetime import datetime

from peewee import CharField, SQL, DateTimeField

from app.models import BaseModel, db


class User(BaseModel):
    email = CharField(constraints=[SQL('NULL')], unique=True)
    password_hash = CharField(constraints=[SQL('NULL')])
    created_at = DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'user'

    @classmethod
    def user_exists(cls, email):
        if db.is_closed():
            db.connect()

        try:
            e: User = cls.get(
                (
                    cls.email == email,
                )
            )
            return e

        except cls.DoesNotExist:
            return None

    @classmethod
    def check_user_login(cls, email, hashed_password):
        if db.is_closed():
            db.connect()

        try:
            e: User = cls.get(
                (
                    cls.email == email,
                )
            )

            if e.password_hash == hashed_password:
                return e

            return None
        except cls.DoesNotExist:
            return None

    @classmethod
    def create_user(cls, email, hashed_password):
        if db.is_closed():
            db.connect()

        cls.create(
            email=email,
            password_hash=hashed_password,
        )

        return True


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def validate_password(password):
    return len(password) >= 8


with suppress(Exception):
    User.create_table()
