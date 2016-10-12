from __init__ import app, db, upload_images
from flask import url_for, render_template, request, flash, redirect, jsonify
from models import PostPic
from forms import ImageForm
from random_str import random_generator

@app.route('/json/')
def tstjson():
    return jsonify(name='sahai',id=10,email='iam.saza@gmail.com', keyerr=[0,1,3,4])


#@app.route('/up/', methods=['POST', 'GET'])
@app.route('/up/')
def upload():
    form =  ImageForm(request.form)
    return render_template('upload.html', form=form)


@app.route('/get/', methods=['POST'])
def getpic():
    error = None
    #form =  ImageForm(request.form)
    if  request.method == "POST":
        #if form.validate_on_submit():
        image = request.files.get('image')
        print image
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
                #return redirect(url_for('show', path_id=postpic.link))
                #url_link = "127.0.0.1:5000/showpic/%s" % postpic.link
                return  jsonify( error = "127.0.0.1:5000/showpic/%s" % postpic.link )
                #return jsonify(success="hello")
    return jsonify(error="The image wasn't uploaded",  errorkeys = [0, 1, 3, 4])

    #return render_template('index.html', form=form, error=error)

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

    return render_template('index.html', form=form, error=error)
    

@app.route('/showpic/<path_id>/')
def show(path_id):

    postpic =  PostPic.query.filter_by(link=path_id).first_or_404()
    pic_url =  app.config['SERVER_URL'] + "/showpic/%s" % postpic.link
    #print random_generator()
    return render_template('picshow.html', postpic=postpic, pic_url=pic_url )

# @app.route('/list')
# def list():
#     data = PostPic.query.order_by(PostPic.id)
#     return render_template('list.html', data=data )