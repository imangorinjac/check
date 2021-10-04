from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def fun():

    if request.method == "POST":

        name = request.form["name"]
        var = "mysupersecret"
        if name == var:

            return render_template("drugi.html", ime=name)
        else:

            return render_template("mis.html")
