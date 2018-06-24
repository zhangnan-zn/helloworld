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


@app.route("/fourth")
def fourth():
    return "fourth"


@app.route("/fifth")
def fifth():
    return "fifth"


@app.route("/sixth")
def sixth():
    return "sixth"


@app.route("/seventh")
def seventh():
    return "seventh"


@app.route("/eighth")
def eighth():
    return "eighth"


@app.route("/ninth")
def ninth():
    return "ninth"


@app.route("/tenth")
def tenth():
    return "tenth"


if __name__ == "__main__":
    app.run()
