# -*- coding: utf-8 -*-
from models import TodoItem


def test_create_and_get_item(app):
    text = 'Yoooloooo'
    item = TodoItem(text=text)
    item.save()
    item_fetched = TodoItem.get(
        TodoItem.id==item.id
    )

    assert item.id is not None
    assert item.id == item_fetched.id
