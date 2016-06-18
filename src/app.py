# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


def init_app(app):
    from views import simple_page
    app.register_blueprint(simple_page)
