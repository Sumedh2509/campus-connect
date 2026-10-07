from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///campusconnect.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Post(db.Model): #creating a class of post
    id = db.Column(db.Integer, primary_key=True)  #this will store the number 
    title = db.Column(db.String(200), nullable=False) #this will have title, making nullable false, makes it so u can't leave it empty
    content = db.Column(db.Text, nullable=False) #making a col for content
    topic = db.Column(db.String(100), nullable=False) #making a col for topic


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create-post", methods=["POST"])
def create_post():

    title = request.form["title"]
    content = request.form["content"]
    topic = request.form["topic"]

    post = Post(
        title=title,
        content=content,
        topic=topic
    )

    db.session.add(post)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)