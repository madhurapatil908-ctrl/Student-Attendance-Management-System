import sqlite3

def add_student():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    dept = input("Enter Department: ")

    cursor.execute("INSERT INTO student(name,roll_no,department) VALUES(?,?,?)",(name,roll,dept))

    conn.commit()
    conn.close()

    print("Student Added Successfully")

def view_student():

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student")

    data = cursor.fetchall()

    for row in data:
        print(row)

    conn.close()

def search_student():

    import sqlite3

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    roll = input("Enter Roll Number : ")

    cursor.execute("SELECT * FROM student WHERE roll_no=?", (roll,))

    data = cursor.fetchone()

    if data:
        print("\nStudent Found")
        print("ID :", data[0])
        print("Name :", data[1])
        print("Roll No :", data[2])
        print("Department :", data[3])
    else:
        print("Student Not Found")

    conn.close()

def update_student():

    import sqlite3

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    roll = input("Enter Roll Number : ")

    name = input("Enter New Name : ")

    dept = input("Enter New Department : ")

    cursor.execute(
        "UPDATE student SET name=?, department=? WHERE roll_no=?",
        (name, dept, roll)
    )

    conn.commit()

    print("Student Updated Successfully")

    conn.close()

def delete_student():

    import sqlite3

    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    roll = input("Enter Roll Number : ")

    cursor.execute(
        "DELETE FROM student WHERE roll_no=?",
        (roll,)
    )

    conn.commit()

    print("Student Deleted Successfully")

    conn.close()    