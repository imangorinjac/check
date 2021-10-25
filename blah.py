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
def fun():

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        confirm_password = ""

        if password == confirm_password:

            return render_template("mis.html", ime=name, users=User.query.all())
        else:
            message = "sorry wrong password"
            return render_template("drugi.html", poruka=message, ime=name)
    else:

        return render_template("sign_up.html")


@app.route("/new", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        if not request.form["username"] or not request.form["password"]:
            print("jfjjej")
        else:
            users = User(request.form["username"], request.form["password"])

            db.session.add(users)
            db.session.commit()
            flash("Record was successfully added")
            return redirect("new")
    return render_template("sign_up.html")
