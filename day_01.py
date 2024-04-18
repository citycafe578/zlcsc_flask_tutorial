#基本架構、導向其他頁面
from flask import Flask, redirect, url_for
app = Flask(__name__ )

@app.route("/")
def home():
    return "hello html, it's flask"

@app.route("/<name>")
def user(name): 
    return f"Hello {name}!"

@app.route("/admin")#重新導向，但是是補充，今天用不到
def admin():
    return redirect(url_for("user", name = "city!"))

if __name__ == "__main__":
    app.run(debug=True)
