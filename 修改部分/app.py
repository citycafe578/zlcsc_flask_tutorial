from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "這裡隨便放"
app.permanent_session_lifetime = timedelta(minutes=1)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_data.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Users(db.Model):  # 修改类名，遵循 PEP 8 命名规范
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
        flash("Login successfully!")  # 增加登录成功消息
        return redirect(url_for("user"))  # 修改为正确的路由
    else:
        if "user" in session:
            return redirect(url_for("user"))  # 修改为正确的路由
        return render_template("day_05_login.html")

@app.route("/user", methods=["POST", "GET"])  # 修改路由名称
def user():
    if "user" in session:
        email = None
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")  # 增加保存邮箱成功消息
        else:
            if "email" in session:
                email = session["email"]
        return render_template("day_05-1user.html", email=email)
    else:
        flash("You are not logged in!")  # 增加未登录提示消息
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("You have been logged out!", "info")  # 增加登出成功消息
    return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
