from __init__ import app, db, upload_images
from flask import url_for, render_template, request, flash, redirect, jsonify
from models import PostPic
from forms import ImageForm
from random_str import random_generator

list_per_page = 10

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

@app.route('/list')
#@app.route('/list/page')
def list():
    # new_page = None
    # new_page  = request.args.get('page')
    page =  request.args.get('page', type=int, default=1)
    y =  request.args
    for x in y:
        print x
        print y[x]
    # if new_page is not None:
    #     page = int(new_page)
    #print new_page
    #data = PostPic.query.order_by(PostPic.id).limit(50).from_self().paginate(page, list_per_page)
    data = PostPic.query.order_by(PostPic.id).paginate(page, list_per_page)
    return render_template('list.html', data=data)



#------------------------
    # 5. Databases
    #     posts = [dict(title=row[0],description=row[1]) for row in cur.fetchall()]

    #     x =  (('a1','a2'),('b1','b2'),('c1','c2'))
    #     posts=[dict(t=row[0],d=row[1])  for  row in x ]
    #     [{'d': 'a2', 't': 'a1'}, {'d': 'b2', 't': 'b1'}, {'d': 'c2', 't': 'c1'}]

    #     for z in posts:
    #         print z['d']

    #     #
    #     x={ 'a': 'hello', 'b': 'bello', 'c': 'cello' }
    #     >>> x.keys()
    #     ['a', 'c', 'b']

    # >>> x.values()
    #     ['hello', 'cello', 'bello']

    #     >>> for v in x:
    #     ...     print "%s:%s" %( v, x[v])
    #     ...
    #     a:hello
    #     c:cello
    #     b:bello
