from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure CI/CD Demo Running"

@app.route("/search")
def search():
    query = request.args.get("q")

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # Secure version (Prevents SQL Injection)
    cursor.execute("SELECT * FROM users WHERE name = ?", (query,))
    results = cursor.fetchall()

    return f"Results: {results}"

if __name__ == "__main__":
    app.run(debug=True)

