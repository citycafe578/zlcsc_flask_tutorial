from flask import Flask, render_template, request, redirect, url_for, session
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
        session.permanent = True #把 permanent 打開，默認為 False
        user = request.form["nm"]
        session["user"] = user  #創建一個session
        return redirect(url_for("user", usr = user))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("day_03_login.html")

@app.route("/usr")
def user():
    if "user" in session:
        usr = session["user"]
        return f"<h1>hello, {usr}!</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)