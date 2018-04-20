from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewTaskForm(FlaskForm):
	task = StringField('Task:', validators=[DataRequired()])
	submit = SubmitField('Add')