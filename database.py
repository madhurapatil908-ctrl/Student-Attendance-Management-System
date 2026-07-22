import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
roll_no TEXT,
department TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER,
date TEXT,
status TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")