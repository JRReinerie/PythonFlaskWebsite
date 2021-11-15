from flask import *
from datetime import *
from ApiCall import apicall
from PasswordGenerator import passwordGenerator

app = Flask(__name__)
app.register_blueprint(apicall, url_prefix="")
app.register_blueprint(passwordGenerator, url_prefix="")
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=1)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", data="tttt")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")


@app.route("/logout", methods=["POST", "GET"])
def logout():
    if request.method == 'POST':
        session.pop("user", None)
        return redirect(url_for("login"))


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", data=user)
    else:
        return redirect(url_for("login"))


if __name__ == "main":
    app.run()
