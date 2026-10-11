from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>Velocity IDE Flask Server</title></head>
    <body style="font-family: sans-serif; background: #0f172a; color: #f8fafc; text-align: center; padding: 50px;">
        <h1 style="color: #38bdf8;">⚡ Hello from Velocity IDE!</h1>
        <p style="font-size: 18px;">Your Python Flask server is successfully running live on Android!</p>
        <p style="color: #94a3b8;">Port: 5000 | Host: 0.0.0.0</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    print("* Velocity IDE: Starting Flask Server...")
    print("* Running on http://127.0.0.1:5000 and http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000)
