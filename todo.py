from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '771e8580908cfa121978b1639607c03d'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Tasks_Add(FlaskForm):
    description = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<Task {self.id}: {self.description}'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Tasks_Add()

    if form.validate_on_submit():
        new_task = Task(description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
        redirect(url_for('index'))
    tasks = Task.query.all()
    return render_template('index.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)