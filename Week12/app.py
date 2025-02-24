from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about/<name>/<int:number>")
def about(name, number):
    return render_template("about.html", name=name, number=number)


if __name__ == "__main__":
    app.run(debug=True)
