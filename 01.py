from flask import Flask

app = Flask(__name__)


@app.route("/member")
def member():
    return "Hello Member!"


if __name__ == "__main__":
    app.run(debug=True)
