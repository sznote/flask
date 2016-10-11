from __init__ import app, db, upload_images
from flask import url_for, render_template, request, flash, redirect
from models import PostPic
from forms import ImageForm
from random_str import random_generator

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    form =  ImageForm(request.form)
    if  request.method == "POST":
        if form.validate_on_submit():
            image = request.files.get('image')
            #print image
            filename = None
            #title = str(image.filename).rsplit('.',1)[0]
            if image:
                # postpic = PostPic(None)
                # db.session.add(postpic)
                # db.session.flush()
                # import pdb; pdb.set_trace()
                # print postpic.id
                try:
                    #filename =  upload_images.save(image, folder=str(postpic.id))
                    filename =  upload_images.save(image)
                except:
                    flash("The images was not uploaded")
                if filename: 
                    #print image.url   
                    link =  random_generator().lower()
                    postpic=PostPic(filename,link)
                    db.session.add(postpic)
                    db.session.commit()
                    return redirect(url_for('show', path_id=postpic.link))

    return render_template('upload.html', form=form, error=error)
    

@app.route('/showpic/<path_id>/')
def show(path_id):

    postpic =  PostPic.query.filter_by(link=path_id).first_or_404()
    print random_generator()
    return render_template('picshow.html', postpic=postpic)

@app.route('/list')
def list():
    data = PostPic.query.order_by(PostPic.id)
    return render_template('list.html', data=data )