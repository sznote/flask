from init import app, bcrypt, db, uploaded_images
from flask import Flask, render_template, url_for, redirect, request, flash, session, abort
from form import registerForm, SetupForm, LoginForm, PostForm
from functools import wraps
from models import Blog, User, Post, Category
from slugify import slugify

#from models import Blog, User, Category, Post
#from form import registerForm, SetupForm, LoginForm, PostForm

POSTS_PER_PAGE = 5

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function



def author_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('is_author') is None:
            return abort(404)
        return f(*args, **kwargs)
    return decorated_function



# @app.route('/')
# def  show_url_for():
#   #return redirect( url_for('show_user_profile', username='sahai') )
#   return url_for('show_user_profile', username='sahai') 

# @app.route('/profile/<username>')
# def show_user_profile(username):
#   return "User: %s" % username

@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page=1):
    blog =  Blog.query.first()
    posts = Post.query.order_by(Post.publish_date.desc()).paginate(page, POSTS_PER_PAGE, False)
    return render_template('index.html', blog=blog, posts=posts)

@app.route('/admin')
@app.route('/admin/<int:page>')
@author_required
def admin(page=1):
    post = Post.query.order_by(Post.publish_date.desc()).paginate(page, POSTS_PER_PAGE, False)
    #if 'username' in session:
    #blogs = Blog.query.count()
    #if blogs  == 0:
    #    return redirect(url_for('setup'))
    return render_template('admin.html', posts=post)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in',None)
    session.pop('username',None)
    session.pop('is_author', None)
    return redirect(url_for('login'))

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    return  render_template("admin.html")




@app.route('/setup',methods=['GET','POST'])
def setup():
    blog = Blog.query.first()
    if blog is not None:
        return redirect(url_for('admin'))

    form =  SetupForm(request.form)   
    error = None     
    if form.validate_on_submit():
        user =  User(
            form.fullname.data , 
            form.email.data, 
            form.username.data, 
            form.password.data,
            True
        )

        db.session.add(user)
        db.session.flush()
        #db.session.commit()
        if user.id:
           
            blog = Blog(form.username.data,user.id)
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user"
        
        if user.id and blog.id:
            db.session.commit()
            flash("Blog Created")
            return redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = "Error create blog"

    return render_template("setup.html",  form=form)


@app.route('/register',methods=['GET', 'POST'])
def register():
    form = registerForm(request.form)
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('user/register.html', form=form)

@app.route('/success')
def success():
    return "Author registered!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    form = LoginForm(request.form)

    if request.method == 'POST':
        # if valid_login(
        #         request.form['username'], 
        #         request.form['password']):
        #     return "Welcome Back,  %s" % request.form.get('username')
        # else:
        #     error = "Incorrent username and password"
        if  form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user:
                if bcrypt.check_password_hash(user.password, form.password.data):
                    session['username'] = form.username.data
                    session['is_author'] = user.is_author
                    return redirect('/login_success')
            error ='Incorrect password'

            # user = User.query.filter_by(
            #  username=form.username.data,
            #  password=form.password.data).limit(1)
            
    return render_template("user/login.html", error=error, form=form)

@app.route('/login_success')
def login_success():
    return  'Author login !!'


def valid_login(username,password):
    #checks on the db if the nameme and password are correct.
    if username == password:
        return True
    else:
        return False


@app.route('/login2', methods=['GET', 'POST'])
def login2():
    if request.values:
    #if request.method == 'POST':
        bar = request.args.to_dict()
        for  x in bar:
                print "%s :: %s " % ( x, bar[x])

        #return  "User is %s" %  request.args.get('username')
        return render_template("login2.html", bar=bar)

        #return  "User is %s" %  request.values['username']
        #http://127.0.0.1:5000/login?username=saahai
    else:
        return '<form method="get" action="/login2"> \
            <p> \
            <input type="text" name="username" placeholder="username" required /> \
            </p> \
            <input type="password" name="password" placeholder="password" /> \
            <p> \
            <input type="submit" formnovalidate  value="submit" /> \
            <button type="submit"  > Summit </button> </p> </form>'

@app.route('/post', methods=['GET', 'POST'])
@author_required
def post():
    form = PostForm(request.form)
    
    if request.method == "POST":
        #import pdb; pdb.set_trace() 
        test = request.files['image']
        image = request.files.get('image')
        imagedata = form.image.data
        #print image
        #image =form.i
        filename = None

        try:
            filename = uploaded_images.save(image, folder='100')
        except:
            flash("The image was not uploaded")

        if form.validate_on_submit():
            if  form.new_category.data :
                new_category = Category(form.new_category.data)
                db.session.add(new_category)
                db.session.flash()
                category = new_category
            else:
                category = form.category.data
            blog = Blog.query.first()
            author = User.query.filter_by(username=session['username']).first()
            title = form.title.data
            body = form.body.data
            slug = slugify(title)
            post = Post(blog, author, title, body, category, slug, filename)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('article', slug=slug ))
    return render_template('post.html', form=form, action="new")
    
@app.route('/article/<slug>')
def article(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    #print post.image
    #print  post.imgsrc
    #print  uploaded_images.url(post.image)
    return  render_template('article.html', post=post)

@app.route('/edit/<int:post_id>',methods=['GET', 'POST'])
def edit(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    form = PostForm(obj=post)
    if form.validate_on_submit():
        original_image = post.image
        #import pdb; pdb.set_trace()
        form.populate_obj(post)
        if  form.image.has_file():
            image = request.files.get('image')
            
            try:
                filename = uploaded_images.save(image)
            except:
                flash("The image was not uploaded")
            if filename:
                post.image = filename
        else:
            post.image = original_image

        if form.new_category.data:
            new_category = Category(form.new_category.data)
            db.session.add(new_category)
            db.session.flash()
            post.category =  new_category
        db.session.commit()

        return  redirect(url_for('article', slug=post.slug))

    return render_template('post.html', form=form, post=post)

@app.route('/delete/<int:post_id>')
def delete(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    post.live = False
    db.session.commit()
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)