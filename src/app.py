# -*- coding: utf-8 -*-
import os
import sys

from flask import Flask

SRC_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.append(SRC_ROOT)

app = Flask(__name__)


def init_app(app, test=False):
    if test:
        app.config['TESTING'] = True

    from views import simple_page
    app.register_blueprint(simple_page)

    from models import init_models
    init_models(app)
