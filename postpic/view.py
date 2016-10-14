from __init__ import app, db, upload_images
from flask import url_for, render_template, request, flash, redirect, jsonify, session, abort
from models import PostPic
from forms import ImageForm, ListForm, LoginForm
from random_str import random_generator
from functools import wraps
import os

list_per_page = 9

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:  #session.get('logged_in') is None
            return abort(404)
        return f(*args, **kwargs)
            #return redirect(url_for('login'))
    return decorated_function


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

@app.route('/admin/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    #session.clear()
    return redirect(url_for('login'))


@app.route('/admin/login', methods=["GET", "POST"])
def login():
    error = None
    form = LoginForm(request.form)
    if form.validate_on_submit():
        usr = form.username.data 
        mypas =  form.password.data
        if usr == 'admin' and mypas == 'admin':
            session['logged_in'] = True
            return  redirect ( url_for('list') ) 
    return  render_template('login.html', form=form, error=error)


class  Dic2obj(object):
    def __init__(self, **entries): 
        self.__dict__.update(entries)


@app.route('/list', methods=["GET", "POST"])
#@login_required
#@app.route('/list/page')
def list():
    # new_page = None
    # new_page  = request.args.get('page')
    #form = ListFrom(request.form)
    # if request.method == "POST":
    #     print  form.username.data 
    
    post = {
            "username" : "sahai",
            'email': "sahai@yahoo.com",
            'country_code': 64210,
        }

    objpost =  Dic2obj(**post)
    form = ListForm(request.form, obj=objpost )
   
   # boxs  = request.form
    if request.method == "POST":
        images_id  = request.form.getlist("imageid")
        
    #print image_id
        for  image_id in images_id:
            postpic = PostPic.query.filter_by(id=image_id).first()
            #imagefile = "%s/%s" %( app.config['UPLOADED_IMAGES_DEST'], PostPic.query.filter_by(id=image_id).first().image)
            if postpic.image is not None:
                imagefile = os.path.join(app.config['UPLOADED_IMAGES_DEST'], 
                    postpic.image)
            
                #print PostPic.query.filter_by(id=image_id).first().image
                #print imagefile
                if os.path.isfile(imagefile):
                    print imagefile +  " :OK"
                    #Delete file 
                    os.remove(imagefile)
                else:
                    print imagefile + " :Not found!"
            #delete database
            #or Postfic.query.filter_by(id=image_id).delete()
            db.session.delete(postpic)
            db.session.commit()
    #redirect       
    #print "username is %s" % request.args.get('username')

    page =  request.args.get('page', type=int, default=1)

    #print form.username.data
    # y =  request.args
    # for x in y:
    #     print x
    #     print y[x]
    # if new_page is not None:
    #     page = int(new_page)
    #print new_page
    #data = PostPic.query.order_by(PostPic.id).limit(50).from_self().paginate(page, list_per_page)
    
    data = PostPic.query.order_by(PostPic.id).paginate(page, list_per_page, error_out=False)
    #print data.pages
    #print page
    if   int(data.pages) <  int(page):

       #print "wtf"
        return redirect ( "%s?page=%s" %( url_for('list'), data.pages ) )
    
        #page = data.pages
        #data = PostPic.query.order_by(PostPic.id).paginate(page, list_per_page, error_out=False)
        #print "wtf"

    return render_template('list.html', data=data, form=form)


##--- delete row
#>>> PostPic.query.filter_by(id=1).delete()
#1
#>>> PostPic.commit()



#---------
#http://www.blog.pythonlibrary.org/2014/02/14/python-101-how-to-change-a-dict-into-a-class/
# class Dict2Obj(object):
#     """
#     Turns a dictionary into a class
#     """
 
#     #----------------------------------------------------------------------
#     def __init__(self, dictionary):
#         """Constructor"""
#         for key in dictionary:
#             setattr(self, key, dictionary[key])
 
 
# #----------------------------------------------------------------------
# if __name__ == "__main__":
#     ball_dict = {"color":"blue",
#                  "size":"8 inches",
#                  "material":"rubber"}
#     ball = Dict2Obj(ball_dict)


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
