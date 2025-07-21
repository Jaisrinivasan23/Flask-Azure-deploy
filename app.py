from flask import Flask, render_template, request
import pyodbc
from config import DB_CONFIG

app = Flask(__name__)

# Connect to Azure SQL
conn = pyodbc.connect(DB_CONFIG)
cursor = conn.cursor()

@app.route('/')
def home():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    return 'User added! <a href="/">Go Back</a>'

if __name__ == '__main__':
    app.run(debug=True)
