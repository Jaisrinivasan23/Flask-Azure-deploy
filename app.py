from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Velocity-IDE!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=500)
