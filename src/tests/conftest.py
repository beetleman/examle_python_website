# -*- coding: utf-8 -*-

import os
import sys
import pytest

TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_ROOT = os.path.dirname(TESTS_ROOT)
sys.path.append(SRC_ROOT)


from app import app as _app


@pytest.yield_fixture()
def app():
    with _app.app_context():
        yield _app


@pytest.yield_fixture()
def client(app):
    client = app.test_client()
    client.testing = True
    yield client
