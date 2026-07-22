from student import add_student, view_student, search_student, update_student, delete_student

from attendance import mark_attendance, view_attendance

from report import attendance_report


while True:

    print("\n===== Student Attendance System =====")
    print("1.Add Student")
    print("2.View Student")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Mark Attendance")
    print("7.View Attendance")
    print("8.Attendance Report")
    print("9.Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_student()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()   

    elif choice == 5:
        delete_student()

    elif choice == 6:
        mark_attendance()

    elif choice == 7:
        view_attendance()

    elif choice == 8:
        attendance_report()

    elif choice == 9:
        break