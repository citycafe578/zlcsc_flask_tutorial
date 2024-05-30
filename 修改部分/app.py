from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "這裡隨便放"
app.permanent_session_lifetime = timedelta(minutes=1)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_data.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Users(db.Model):  #
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return render_template("day_02_base.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True 
        user = request.form["nm"]
        session["user"] = user
        flash("Login successfully!")  # 
        return redirect(url_for("user"))  # 
    else:
        if "user" in session:
            return redirect(url_for("user"))  #
        return render_template("day_05_login.html")

@app.route("/user", methods=["POST", "GET"])  # 
def user():
    if "user" in session:
        email = None
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("day_05-1user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("You have been logged out!", "info")  # 
    return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
