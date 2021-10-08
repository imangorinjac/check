
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///registration.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
@app.route("/", methods=["GET", "POST"])
def fun():

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        var = "mysupersecret"
        if password == var:

            return render_template("drugi.html", ime=name)
        else:
            message = "sorry wrong password"
            return render_template("mis.html", poruka=message)
    else:

        return render_template("mis.html")