# -*- coding: utf-8 -*-
from datetime import datetime

from peewee import SqliteDatabase, Proxy, Model, TextField, DateTimeField


database_proxy = Proxy()


class BaseModel(Model):
    created_date = DateTimeField(default=datetime.now)

    class Meta:
        database = database_proxy


class TodoItem(Model):
    text = TextField()


def init_models(app):
    if app.config['TESTING']:
        database = SqliteDatabase(':memory:')
    else:
        database = SqliteDatabase('local.db')

    database_proxy.initialize(database)
    database.connect()
    database.create_tables([
        TodoItem,
    ], safe=True)
