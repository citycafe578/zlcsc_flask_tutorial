#連結至index.html，然後從py傳訊息過去，以及在html寫py
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("day_02.html", content = name, a = 12345) #傳一些簡單的小東西



if __name__ == "__main__":
    app.run(debug=True)
