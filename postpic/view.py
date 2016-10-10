from __init__ import app, db
from flask import url_for, render_template, request, flash, redirect
from models import PostPic
from forms import ImageForm

@app.route('/', methods=['GET', 'POST'])
def index():
	error = None
	form =  ImageForm(request.form)
	if form.validate_on_submit():
		postpic  = PostPic(form.image.data)
		db.session.add(postpic)
		db.session.commit()
		return redirect(url_for('index'))

	return render_template('upload.html', form=form, error=error)
	

@app.route('/<int:path_id>/<slug>')
def show():
	return render_template('picshow.html')

@app.route('/list')
def list():
	data = PostPic.query.order_by(PostPic.id)
	return render_template('list.html', data=data )