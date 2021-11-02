from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///registration.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "random string"
db = SQLAlchemy(app)


class User(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):

        self.username = username
        self.password = password


db.create_all()


@app.route("/", methods=["GET", "POST"])
def login():
    password = ""
    username = ""
    password = User.query().get(password=password)
    username = User.query().get(username=username)

    return render_template("mis.html")


@app.route("/new", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        confirm_password = request.form.get("confirm_password", None)
        if username is None or password is None or confirm_password is None:
            print("Some value is None!")
            return render_template("sign_up.html")
        if password != confirm_password:
            print("Password doesn't match confirm password!")
            return render_template("sign_up.html")

        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        flash("Record was successfully added")
        print("Record was successfully added")
        return render_template("sign_up.html")
    return render_template("sign_up.html")
