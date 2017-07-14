from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
'''app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:2483618j@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(120))
    blog_text = db.Column(db.String(2000))

    def __init__ (self, blog_title)
        self.blog_title = blog_title
        self.blog_text = blog_text
'''

blog_list = []

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        blog_title = request.form['blog_title']
        new_blog = request.form['new_blog']
        
        #db.session.add(new_task)
        #db.session.commit()

    #tasks = Task.query.filter_by(completed=False).all()
    return render_template('blog_post.html',title="Build a Blog!")
        

app.run()