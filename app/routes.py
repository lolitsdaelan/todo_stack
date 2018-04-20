from flask import render_template, flash, redirect
from app import app
from app.forms import NewTaskForm


@app.route('/index', methods=['GET', 'POST'])
def index():
	form = NewTaskForm()
	if form.validate_on_submit():
		flash('You just added the following task: {}'.format(
			form.task.data))
		return redirect('/index')
	return render_template('index.html', form=form)