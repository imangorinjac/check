from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///registration.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class User(db.Model):
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    confirm_password = db.Column(db.String(120), nullable=False)


def __init__(self, username, password, confirm_password):
    self.username = username
    self.password = password
    self.confirm_password = confirm_password


db.create_all()


@app.route("/", methods=["GET", "POST"])
def fun():

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        var = "mysupersecret"
        if password == var:

            return render_template("sign_up.html", ime=name, users=User.query.all())
        else:
            message = "sorry wrong password"
            return render_template("mis.html", poruka=message)
    else:

        return render_template("sign_up.html")


@app.route("/new", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        if (
            not request.form["username"]
            or not request.form["password"]
            or not request.form["confirm_password"]
        ):
            return render_template("mis.html")

        else:

            user = User(
                request.form["username"],
                request.form["password"],
                request.files["confirm_password"],
            )

        db.session.add(User)
        db.session.commit()

        return redirect("mis")

    return render_template("sign_up.html", korisnici=User)
