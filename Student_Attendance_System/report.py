import sqlite3

def attendance_report():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT student.name,
           COUNT(attendance.id)
    FROM student
    LEFT JOIN attendance
    ON student.id = attendance.student_id
    GROUP BY student.id
    """)

    data = cursor.fetchall()

    print("\nAttendance Report\n")

    for row in data:
        print("Name :", row[0])
        print("Total Attendance :", row[1])
        print("-------------------")

    conn.close()