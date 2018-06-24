from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"


@app.route("/second")
def second():
    return "second"


@app.route("/third")
def third():
    return "third"


if __name__ == "__main__":
    app.run()
