# -*- coding: utf-8 -*-
from models import TodoItem


def test_create_and_get_item(app):
    text = 'Yoooloooo'
    item = TodoItem(text=text)
    item.save()
    item_fetched = TodoItem.select().where(
        TodoItem.id==item.id
    ).get()

    assert item.id is not None
    assert item.id == item_fetched.id
