import pymysql
from peewee import (
    Model,
    MySQLDatabase
)
from playhouse.shortcuts import ReconnectMixin


from app.settings import Config


class ReconnectMySQLDatabase(ReconnectMixin, MySQLDatabase):
    pass


try:
    connection = pymysql.connect(
        database=Config.DB_NAME,
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )

except pymysql.OperationalError as er:
    connection = pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )
    cursor = connection.cursor()
    cursor.execute(f'CREATE SCHEMA {Config.DB_NAME}')
    cursor.execute(f'USE {Config.DB_NAME}')
    cursor.close()
    connection.close()

finally:
    db = ReconnectMySQLDatabase(
        database=Config.DB_NAME,
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )


class BaseModel(Model):
    class Meta:
        database = db
