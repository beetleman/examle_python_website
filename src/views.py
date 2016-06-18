from flask import render_template, Blueprint

simple_page = Blueprint(
    'simple_page', __name__,
    template_folder='templates'
)


@simple_page.route('/')
def index():
    return render_template('index.html')
