#把每一個網頁都會相同的html寫在一起(base template)
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("day_02_index.html")



if __name__ == "__main__":
    app.run(debug=True)

