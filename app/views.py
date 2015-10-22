from flask import render_template, flash, redirect
from app import app
from .forms import TaskForm

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': True
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/')
@app.route('/tasks', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.title.data, str(form.description.data)))
    return render_template('index.html',
                           tasks = tasks,
                           form = form)
