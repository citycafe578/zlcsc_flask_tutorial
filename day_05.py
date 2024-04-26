from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta #計算時間差

app = Flask(__name__)
app.secret_key = "這裡隨便放"
app.permanent_session_lifetime = timedelta(minutes=1)


@app.route("/")
def home():
    return render_template("day_02_index.html")

@app.route("/login", methods = ["POST" ,"GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Succesful!")
        return redirect(url_for("user", usr = user))
    else:
        if "user" in session:
            flash("U have been logged in!")
            return redirect(url_for("user"))
        return render_template("day_05_login.html")
@app.route("/usr")
def user():
    if "user" in session:
        usr = session["user"]
        return render_template("day_05_user.html", user = usr)
    else:
        flash("U r not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out!")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)