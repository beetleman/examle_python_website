# -*- coding: utf-8 -*-
from flask import render_template, Blueprint, request
from flask.views import MethodView

from models import TodoItem


simple_page = Blueprint(
    'simple_page', __name__,
    template_folder='templates'
)


@simple_page.route('/')
def index():
    return render_template('index.html')


class ToDoListView(MethodView):

    def render_todo(self):
        items = TodoItem.select()
        return render_template('todo.html', items=items)

    def get(self):
        return self.render_todo()

    def post(self):
        text = request.form.get('text')
        item = TodoItem(text=text)
        item.save()
        return self.render_todo()


simple_page.add_url_rule('/todo/', view_func=ToDoListView.as_view('todo'))
