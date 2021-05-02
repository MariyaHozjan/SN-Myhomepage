from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/Hairsalon")
def hair_salon():
    return render_template("Hairsalon.html")

@app.route("/fakebook")
def fakebook():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(use_reloader=True)