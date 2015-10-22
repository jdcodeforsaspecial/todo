from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class TaskForm(Form):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description', default='')
