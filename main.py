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


if __name__ == "__main__":
    print "Run server"
    app.run()
