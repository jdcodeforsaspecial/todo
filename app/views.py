from flask import render_template, flash, redirect
from app import app, db, models
from .forms import TaskForm

@app.route('/')
@app.route('/tasks', methods=['GET', 'POST'])
def task_collection():
    form = TaskForm()
    if form.validate_on_submit():
        add_task(form.title.data,
                 form.description.data)
    tasks = models.Task.query.all()
    return render_template('index.html',
                           tasks = tasks,
                           form = form)

def add_task(title, description):
    task = models.Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()
