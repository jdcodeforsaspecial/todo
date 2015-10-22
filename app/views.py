from flask import render_template, flash, redirect
from app import app, models
from .forms import TaskForm

@app.route('/')
@app.route('/tasks', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.title.data, str(form.description.data)))
    tasks = models.Task.query.all()
    return render_template('index.html',
                           tasks = tasks,
                           form = form)
