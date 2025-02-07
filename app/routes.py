from flask import render_template, redirect, url_for
from app import app
from app.models import Task

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html')

@app.route('/completed/<int:task_id')
def complete_task(task_id):
    task = Task.query.get(task_id) # Find task by ID
    if task:
        task.completed = not task.completed # Toggle completed status
        db.session.commit()
    return redirect(url_for('index'))