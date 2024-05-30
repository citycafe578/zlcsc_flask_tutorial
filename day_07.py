from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta #計算時間差
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "這裡隨便放"
app.permanent_session_lifetime = timedelta(minutes=1)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///user_data.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    return render_template("day_02_index.html")

@app.route("/login", methods = ["POST" ,"GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        #當使用者輸入名稱後確認是否已經註冊\
        found_user = users.query.filter_by(name = user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")#這裡的 users 是我們上一堂課裡面的class
            db.session.add(usr)
            db.session.commit()

        flash("Login Succesful!")
        return redirect(url_for("user", usr = user))
    else:
        if "user" in session:
            flash("U have been logged in!")
            return redirect(url_for("user"))
        return render_template("day_05_login.html")
@app.route("/usr", methods = ["POST", "GET"])
def user():
    if "user" in session:
        usr = session["user"]
        email = None
        if request.method == "POST": #在這裡做跟之前輸入名稱時一模一樣的事
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name = usr).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!!")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("day_05_user.html", email = email)
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

@app.route("/view")
def view():
    return render_template("view.html", values = users.query.all())

if __name__ == "__main__":
    # db.create_all()這是舊的寫法
    with app.app_context():
        db.create_all()
    app.run(debug = True)