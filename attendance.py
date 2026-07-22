import sqlite3
from datetime import date

def mark_attendance():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    roll = input("Enter Roll Number : ")

    cursor.execute(
        "SELECT id FROM student WHERE roll_no=?",
        (roll,)
    )

    student = cursor.fetchone()

    if student:

        status = input("Present or Absent : ")

        today = date.today()

        cursor.execute(
            "INSERT INTO attendance(student_id,date,status) VALUES(?,?,?)",
            (student[0], str(today), status)
        )

        conn.commit()

        print("Attendance Saved")

    else:

        print("Student Not Found")

    conn.close()

def view_attendance():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT student.name,
           student.roll_no,
           attendance.date,
           attendance.status
    FROM student
    JOIN attendance
    ON student.id = attendance.student_id
    """)

    data = cursor.fetchall()

    for row in data:
        print(row)

    conn.close()