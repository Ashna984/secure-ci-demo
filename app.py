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
    sql = "SELECT * FROM users WHERE name = '" + query + "'"  # SQL Injection
    cursor.execute(sql)
    return "Search Complete"

if __name__ == "__main__":
    app.run(debug=True)
