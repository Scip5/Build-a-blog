from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:2483618j@localhost:8889/build-a-blog'
app.config['SQLACHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(100))
    blog_post = db.Column(db.String(1200))

    def __init__(self, blog_title, blog_post):
        self.blog_title = blog_title
        self.blog_post = blog_post




@app.route('/newpost', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        titleError = ""
        postError = ""
        blogTitle = request.form['blog_title']
        blogPost = request.form['new_blog']

        if len(blogTitle) == 0 or len(blogTitle) >= 100:
            titleError = "Your title is too long, or you did not input anything. Try again."
            blogTitle = ""
        if len(blogPost) == 0 or len(blogPost) >= 1200:
            postError = "Your post is too long, or you did not input anything. Try again."
            blogPost = ""

        if  len(titleError) > 0 and len(postError) > 0:
            return render_template('blog_post.html', titleError = titleError,
            postError=postError, blog_title=blogTitle, new_blog=blogPost)

        else:
            new_blog_post = Blog(blogTitle, blogPost)
            db.session.add(new_blog_post)
            db.session.commit()
            return redirect("/blog?id=" + str(new_blog_post.id))

    else:
        blogs = Blog.query.all()

    return render_template('blog_post.html', blogs=blogs)

@app.route('/blog', methods=['GET'])
def add():
    blog_id = request.args.get('id')
    if blog_id == None:
        blogs = Blog.query.all()
        return render_template('blog_main.html', blogs=blogs)
    else:
        single_post = Blog.query.filter_by(id=blog_id).first()
        return render_template('individual_post.html', blogs=single_post)

        
if __name__ == '__main__':
    app.run()