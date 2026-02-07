import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("INSERT INTO users (name) VALUES ('admin')")
cursor.execute("INSERT INTO users (name) VALUES ('ashna')")
cursor.execute("INSERT INTO users (name) VALUES ('testuser')")

conn.commit()
conn.close()

print("Database setup completed successfully.")
