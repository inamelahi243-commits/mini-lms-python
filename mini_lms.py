"""
Mini LMS - Learning Management System
=====================================
A console-based LMS with Student, Teacher and Administrator portals.
"""

# ============================================================
#                      CONFIGURATION
# ============================================================

WIDTH = 62
INNER = WIDTH - 4  # usable text width inside a box


# ============================================================
#                    INTERFACE FUNCTIONS
# ============================================================

def line(char="═"):
    print(char * WIDTH)


def title(text):
    print()
    print("╔" + "═" * (WIDTH - 2) + "╗")
    print("║" + text.center(WIDTH - 2) + "║")
    print("╚" + "═" * (WIDTH - 2) + "╝")


def section(text):
    print()
    print("┌" + "─" * (WIDTH - 2) + "┐")
    print("│" + text.center(WIDTH - 2) + "│")
    print("└" + "─" * (WIDTH - 2) + "┘")


def card(rows, heading=None, double=False):
    """Print a bordered card. `rows` is a list of (label, value) pairs."""
    tl, tr, bl, br, h, v, ml, mr = (
        ("╔", "╗", "╚", "╝", "═", "║", "╠", "╣") if double
        else ("┌", "┐", "└", "┘", "─", "│", "├", "┤")
    )
    print()
    print(tl + h * (WIDTH - 2) + tr)
    if heading:
        print(v + heading.center(WIDTH - 2) + v)
        print(ml + h * (WIDTH - 2) + mr)
    for label, value in rows:
        text = f"{label:<13}: {value}" if label else ""
        print(f"{v} {text:<{INNER}} {v}")
    print(bl + h * (WIDTH - 2) + br)


def menu(heading, options):
    section(heading)
    print("│" + " " * (WIDTH - 2) + "│")
    for key, text in options:
        print("│" + f"   [{key}]".ljust(8) + text.ljust(WIDTH - 10) + "│")
    print("│" + " " * (WIDTH - 2) + "│")
    print("└" + "─" * (WIDTH - 2) + "┘")


def success(message):
    print(f"\n  [SUCCESS] {message}")


def error(message):
    print(f"\n  [ERROR]   {message}")


def info(message):
    print(f"\n  [INFO]    {message}")


def pause():
    input("\n  Press ENTER to continue...")


def ask(prompt):
    return input(f"  {prompt} → ").strip()


def main_header():
    print()
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║                      M I N I   L M S                       ║")
    print("║                                                            ║")
    print("║               LEARNING MANAGEMENT SYSTEM                   ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")


def role_menu():
    menu("SELECT YOUR ROLE", [
        ("1", "Student"),
        ("2", "Teacher"),
        ("3", "Administrator"),
        ("4", "Exit System"),
    ])


def student_menu():
    menu("STUDENT PORTAL", [
        ("1", "View My Profile"),
        ("2", "View Available Courses"),
        ("3", "Enroll in Course"),
        ("4", "View My Courses"),
        ("5", "View Course Assignments"),
        ("6", "Submit Assignment"),
        ("7", "View My Result"),
        ("8", "Logout"),
    ])


def teacher_menu():
    menu("TEACHER PORTAL", [
        ("1", "View My Profile"),
        ("2", "View My Courses"),
        ("3", "View Course Assignments"),
        ("4", "Create Assignment"),
        ("5", "View Student Submissions"),
        ("6", "Assign Marks"),
        ("7", "View Student Results"),
        ("8", "Logout"),
    ])


def admin_menu():
    menu("ADMINISTRATION PORTAL", [
        ("1", "View Admin Profile"),
        ("2", "Add Student"),
        ("3", "Add Teacher"),
        ("4", "Create Course"),
        ("5", "View All Students"),
        ("6", "View All Teachers"),
        ("7", "View All Courses"),
        ("8", "Remove Student"),
        ("9", "Remove Teacher"),
        ("10", "Remove Course"),
        ("11", "Logout"),
    ])


def logout(name):
    title("LOGOUT")
    print(f"  Goodbye, {name}!")
    print("  Returning to role selection...")


def find_by(items, attr, value):
    """Return the first item whose attribute equals value, else None."""
    return next((i for i in items if getattr(i, attr) == value), None)


def get_grade(percentage):
    if percentage >= 90:
        return "A"
    if percentage >= 80:
        return "A-"
    if percentage >= 70:
        return "B+"
    if percentage >= 65:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 55:
        return "D"
    return "F"


# ============================================================
#                       MODEL CLASSES
# ============================================================

class Student:

    def __init__(self, std_name, std_id, std_email):
        self.std_name = std_name
        self.std_id = std_id
        self.std_email = std_email
        self.courses = []
        self.submission = []

    def __str__(self):
        return (
            f"Student Name : {self.std_name}\n"
            f"Student ID   : {self.std_id}\n"
            f"Email        : {self.std_email}"
        )

    def student_enroll(self, course):
        self.courses.append(course)

    def submit_assignment(self, assignment, course):
        """Submit an assignment. Returns True on success, False otherwise."""
        if course not in self.courses:
            error("You are not enrolled in this course.")
            return False

        if assignment not in course.assignments:
            error("This is not your assigned assignment.")
            return False

        if any(s.assignment == assignment for s in self.submission):
            error("You have already submitted this assignment.")
            return False

        self.submission.append(AssignmentSubmission(self.std_id, assignment))
        return True

    def check_grade(self, percentage, course):
        card([
            ("Student", self.std_name),
            ("Course", course.course_name),
            ("Percentage", f"{percentage:.2f}%"),
            ("Grade", get_grade(percentage)),
        ], heading="GRADE")

    def view_result(self, course):
        if course not in self.courses:
            error("You are not enrolled in this course.")
            return

        if not course.assignments:
            info(f"{course.course_name} has no assignment yet.")
            return

        if not self.submission:
            info(f"{self.std_name} has not submitted any assignment.")
            return

        total_marks = 0
        get_marks = 0
        graded = False

        for assignment in course.assignments:
            total_marks += assignment.assignment_marks

            for submission in self.submission:
                if (
                    submission.assignment == assignment
                    and submission.obtained_marks is not None
                ):
                    get_marks += submission.obtained_marks
                    graded = True

        if not graded:
            info("Your submitted assignments have not been graded yet.")
            return

        if total_marks == 0:
            error("Total marks cannot be zero.")
            return

        percentage = (get_marks * 100) / total_marks

        card([
            ("Student", self.std_name),
            ("Student ID", self.std_id),
            ("Course", course.course_name),
            ("", ""),
            ("Marks", f"{get_marks} / {total_marks}"),
            ("Percentage", f"{percentage:.2f}%"),
        ], heading="STUDENT RESULT", double=True)

        self.check_grade(percentage, course)


class Teacher:

    def __init__(self, tec_name, tec_id):
        self.tec_name = tec_name
        self.tec_id = tec_id
        self.courses = []
        self.submitted_assignment = []
        self.created_assignment = []

    def __str__(self):
        return (
            f"Teacher Name : {self.tec_name}\n"
            f"Teacher ID   : {self.tec_id}"
        )

    def add_course(self, course):
        self.courses.append(course)

    def create_assignment(
        self, course, assignment_id, assignment_title, assignment_marks
    ):
        assignment = Assignment(
            course, assignment_id, assignment_title, assignment_marks
        )
        course.assignments.append(assignment)
        self.created_assignment.append(assignment)

    def assign_marks(self, submission, marks):
        if self.tec_id != submission.assignment.course.course_tutor.tec_id:
            error(
                "You are not authorized to assign marks "
                "to this submission."
            )
            return

        total_marks = submission.assignment.assignment_marks

        if marks < 0 or marks > total_marks:
            error("Invalid marks have been assigned.")
            return

        submission.obtained_marks = marks
        success(f"{marks}/{total_marks} marks assigned successfully.")


class Course:

    def __init__(self, course_name, course_id, course_tutor):
        self.course_name = course_name
        self.course_id = course_id
        self.course_tutor = course_tutor
        self.assignments = []

    def __str__(self):
        return (
            f"Course ID : {self.course_id}\n"
            f"Course    : {self.course_name}\n"
            f"Teacher   : {self.course_tutor.tec_name}"
        )


class Assignment:

    def __init__(
        self, course, assignment_id, assignment_title, assignment_marks
    ):
        self.course = course
        self.assignment_id = assignment_id
        self.assignment_title = assignment_title
        self.assignment_marks = assignment_marks

    def __str__(self):
        return (
            f"Assignment ID : {self.assignment_id}\n"
            f"Title         : {self.assignment_title}\n"
            f"Total Marks   : {self.assignment_marks}"
        )


class AssignmentSubmission:

    def __init__(self, std_id, assignment):
        self.std_id = std_id
        self.assignment = assignment
        self.obtained_marks = None


class Admin:

    def __init__(self, adm_name, adm_id, adm_gmail, adm_profession):
        self.adm_name = adm_name
        self.adm_id = adm_id
        self.adm_gmail = adm_gmail
        self.adm_profession = adm_profession

    def __str__(self):
        return (
            f"Name       : {self.adm_name}\n"
            f"Admin ID   : {self.adm_id}\n"
            f"Email      : {self.adm_gmail}\n"
            f"Profession : {self.adm_profession}"
        )


# ============================================================
#                     LMS DATABASE (IN-MEMORY)
# ============================================================

lms_std_user = []
lms_tec_user = []
lms_admin_user = []
lms_courses = []


def load_sample_data():
    """Populate the LMS with sample students, teachers, courses, admins."""
    lms_std_user.extend([
        Student("Inam", "2025-RIS-1", "inamelahi243@gmail.com"),
        Student("Ali", "2025-RIS-2", "ali243@gmail.com"),
        Student("Zaid", "2025-RIS-3", "zaid456@gmail.com"),
        Student("Iqra Iqbal", "2025-RIS-4", "iqra456@gmail.com"),
        Student("Bisma Batool", "2025-RIS-5", "bisma456@gmail.com"),
    ])

    tec_1 = Teacher("Dr. Shaid", "shaid231_AP_1")
    tec_2 = Teacher("Dr. Ali", "ali342_AC_1")
    tec_3 = Teacher("Dr. Jawad Siddiqui", "jawad342_EM_1")
    tec_4 = Teacher("Ms. Sara Akhtar", "sara383_GD_1")
    tec_5 = Teacher("Mr. Ahmad Siddique", "ahmad235_RC_1")
    lms_tec_user.extend([tec_1, tec_2, tec_3, tec_4, tec_5])

    courses = [
        (Course("Applied Physics", "AP101q", tec_1), tec_1),
        (Course("Applied Chemistry", "AC1039", tec_2), tec_2),
        (Course("Engineering Mechanics", "EM235b", tec_3), tec_3),
        (Course("Graphics and Designing", "GD355a", tec_3), tec_3),
        (Course("Robotics Vision", "Robotics78c", tec_3), tec_3),
    ]
    for course, tutor in courses:
        tutor.add_course(course)
        lms_courses.append(course)

    lms_admin_user.extend([
        Admin("Mustafa Kamal", "ADM001", "mustafa123@gmail.com",
              "Admission Manager"),
        Admin("Khizar Hayat", "ADM002", "khizar123@gmail.com",
              "Academic Coordinator"),
        Admin("Mehmood-ul-Hassan", "ADM003", "mehmood131@gmail.com",
              "Result Manager"),
        Admin("Aqib Hussain", "ADM004", "aqib127@gmail.com", "Clerk"),
        Admin("Thaira Noreen", "ADM005", "noreen123@gmail.com",
              "Examination Officer"),
    ])


# ============================================================
#                      STUDENT PORTAL
# ============================================================

def print_assignments(course):
    for number, assignment in enumerate(course.assignments, start=1):
        print(f"\n  Assignment {number}")
        print("  " + "─" * 33)
        print(f"  ID    : {assignment.assignment_id}")
        print(f"  Title : {assignment.assignment_title}")
        print(f"  Marks : {assignment.assignment_marks}")


def student_portal(student):
    while True:
        title("STUDENT DASHBOARD")
        print(f"  Welcome, {student.std_name}")
        print(f"  Student ID: {student.std_id}")
        student_menu()
        choice = ask("Enter your choice")

        if choice == "1":
            title("MY PROFILE")
            print(student)
            pause()

        elif choice == "2":
            title("AVAILABLE COURSES")
            available = [c for c in lms_courses if c not in student.courses]
            for course in available:
                card([
                    ("Course ID", course.course_id),
                    ("Course", course.course_name),
                    ("Teacher", course.course_tutor.tec_name),
                ])
            if not available:
                info("No new courses are available.")
            pause()

        elif choice == "3":
            title("COURSE ENROLLMENT")
            course_id = ask("Enter the Course ID")
            course = find_by(lms_courses, "course_id", course_id)
            if course is None:
                error(f"Course ID '{course_id}' was not found.")
            elif course in student.courses:
                info(f"You are already enrolled in {course.course_name}.")
            else:
                student.student_enroll(course)
                success(
                    f"You have successfully enrolled in {course.course_name}."
                )
            pause()

        elif choice == "4":
            title("MY COURSES")
            if student.courses:
                for number, course in enumerate(student.courses, start=1):
                    print(
                        f"  [{number}] {course.course_id}  |  "
                        f"{course.course_name}"
                    )
            else:
                info("You are not enrolled in any course.")
            pause()

        elif choice == "5":
            title("COURSE ASSIGNMENTS")
            course = find_by(
                student.courses, "course_id", ask("Enter the Course ID")
            )
            if course is None:
                error("You are not enrolled in this course.")
            else:
                section(course.course_name)
                if course.assignments:
                    print_assignments(course)
                else:
                    info(f"{course.course_name} has no assignments.")
            pause()

        elif choice == "6":
            title("SUBMIT ASSIGNMENT")
            course = find_by(
                student.courses, "course_id", ask("Enter the Course ID")
            )
            if course is None:
                error("You are not enrolled in this course.")
            else:
                print(f"\n  Course: {course.course_name}")
                if not course.assignments:
                    info("This course has no assignments.")
                else:
                    assignment = find_by(
                        course.assignments,
                        "assignment_id",
                        ask("Enter Assignment ID"),
                    )
                    if assignment is None:
                        error("No assignment was found with this ID.")
                    elif student.submit_assignment(assignment, course):
                        success("Assignment submitted successfully.")
            pause()

        elif choice == "7":
            title("VIEW RESULT")
            course = find_by(
                student.courses, "course_id", ask("Enter the Course ID")
            )
            if course is None:
                error("You are not enrolled in this course.")
            else:
                student.view_result(course)
            pause()

        elif choice == "8":
            logout(student.std_name)
            break

        else:
            error("Invalid choice. Please try again.")


# ============================================================
#                      TEACHER PORTAL
# ============================================================

def teacher_submissions(teacher):
    """Yield (student, submission) pairs belonging to the teacher's courses."""
    for std in lms_std_user:
        for submission in std.submission:
            if submission.assignment.course.course_tutor == teacher:
                yield std, submission


def teacher_portal(teacher):
    while True:
        title("TEACHER DASHBOARD")
        print(f"  Welcome, {teacher.tec_name}")
        print(f"  Teacher ID: {teacher.tec_id}")
        teacher_menu()
        choice = ask("Enter your choice")

        if choice == "1":
            title("MY PROFILE")
            print(teacher)
            pause()

        elif choice == "2":
            title("MY COURSES")
            if teacher.courses:
                for number, course in enumerate(teacher.courses, start=1):
                    print(
                        f"\n  [{number}] {course.course_id} | "
                        f"{course.course_name}"
                    )
            else:
                info("You have no courses yet.")
            pause()

        elif choice == "3":
            title("COURSE ASSIGNMENTS")
            if not teacher.courses:
                info("There is no course assigned to you.")
            else:
                course = find_by(
                    teacher.courses, "course_id", ask("Enter your Course ID")
                )
                if course is None:
                    error("This course is not assigned to you.")
                else:
                    section(course.course_name)
                    if course.assignments:
                        print_assignments(course)
                    else:
                        info(
                            "You have not created any assignment "
                            "for this course."
                        )
            pause()

        elif choice == "4":
            title("CREATE ASSIGNMENT")
            course = find_by(
                teacher.courses, "course_id", ask("Enter the Course ID")
            )
            if course is None:
                error("This course is not assigned to you.")
            else:
                print(f"\n  Course: {course.course_name}")
                assignment_id = ask("Assignment ID")
                assignment_title = ask("Assignment Title")
                try:
                    marks = int(ask("Total Marks"))
                    if marks <= 0:
                        error("Marks must be greater than zero.")
                    else:
                        teacher.create_assignment(
                            course, assignment_id, assignment_title, marks
                        )
                        success("Assignment created successfully.")
                except ValueError:
                    error("Please enter a valid number.")
            pause()

        elif choice == "5":
            title("STUDENT SUBMISSIONS")
            count = 0
            for std, submission in teacher_submissions(teacher):
                card([
                    ("Student", std.std_name),
                    ("Assignment", submission.assignment.assignment_title),
                    ("Course", submission.assignment.course.course_name),
                ])
                count += 1
            print(f"\n  Total Submissions: {count}")
            pause()

        elif choice == "6":
            title("ASSIGN MARKS")
            found = False
            for std, submission in teacher_submissions(teacher):
                found = True
                card([
                    ("Student", std.std_name),
                    ("Assignment", submission.assignment.assignment_title),
                    ("Total Marks", submission.assignment.assignment_marks),
                ])
                try:
                    marks = int(ask("Enter Obtained Marks"))
                    teacher.assign_marks(submission, marks)
                except ValueError:
                    error("Please enter a valid number.")
            if not found:
                info("There are no submissions to grade.")
            pause()

        elif choice == "7":
            title("STUDENT RESULTS")
            student_id = ask("Enter Student ID")
            std = find_by(lms_std_user, "std_id", student_id)
            if std is None:
                error(f"Student ID '{student_id}' was not found.")
            else:
                found = False
                for submission in std.submission:
                    if submission.assignment.course.course_tutor == teacher:
                        found = True
                        card([
                            ("Student", std.std_name),
                            ("Course", submission.assignment.course.course_name),
                            ("Assignment", submission.assignment.assignment_title),
                            ("Total Marks", submission.assignment.assignment_marks),
                            ("Obtained", submission.obtained_marks),
                        ])
                if not found:
                    info(
                        f"No result is available for {std.std_name} "
                        f"in your courses."
                    )
            pause()

        elif choice == "8":
            logout(teacher.tec_name)
            break

        else:
            error("Invalid choice. Please try again.")


# ============================================================
#                       ADMIN PORTAL
# ============================================================

def admin_add_student(admin):
    title("ADD STUDENT")
    if admin.adm_profession != "Admission Manager":
        error("You are not authorized to add students.")
        return

    std_id = ask("Student ID")
    if find_by(lms_std_user, "std_id", std_id):
        error(f"Student with ID {std_id} already exists.")
        return

    std_email = ask("Student Email")
    std_name = ask("Student Name")
    lms_std_user.append(Student(std_name, std_id, std_email))
    success(f"Student {std_name} has been admitted successfully.")


def admin_add_teacher(admin):
    title("ADD TEACHER")
    if admin.adm_profession != "Academic Coordinator":
        error("You are not authorized to add teachers.")
        return

    teacher_id = ask("Teacher ID")
    if find_by(lms_tec_user, "tec_id", teacher_id):
        error(f"Teacher with ID {teacher_id} already exists.")
        return

    teacher_name = ask("Teacher Name")
    lms_tec_user.append(Teacher(teacher_name, teacher_id))
    success(f"Teacher {teacher_name} has been added successfully.")


def admin_create_course(admin):
    title("CREATE COURSE")
    if admin.adm_profession != "Academic Coordinator":
        error("You are not authorized to create courses.")
        return

    course_id = ask("Course ID")
    if find_by(lms_courses, "course_id", course_id):
        error(f"Course with ID {course_id} already exists.")
        return

    course_name = ask("Course Name")
    tutor = find_by(lms_tec_user, "tec_id", ask("Teacher ID"))
    if tutor is None:
        error("Invalid Teacher ID.")
        return

    course = Course(course_name, course_id, tutor)
    lms_courses.append(course)
    tutor.add_course(course)
    success(f"Course {course_name} created successfully.")


def admin_list_students():
    title("ALL STUDENTS")
    print(f"\n  Total Students: {len(lms_std_user)}")
    if not lms_std_user:
        info("No student is registered yet.")
    for number, std in enumerate(lms_std_user, start=1):
        print(f"\n  [{number}]")
        print(f"      Name  : {std.std_name}")
        print(f"      ID    : {std.std_id}")
        print(f"      Email : {std.std_email}")


def admin_list_teachers():
    title("ALL TEACHERS")
    print(f"\n  Total Teachers: {len(lms_tec_user)}")
    if not lms_tec_user:
        info("No teacher is registered yet.")
    for number, tec in enumerate(lms_tec_user, start=1):
        print(f"\n  [{number}]")
        print(f"      Name : {tec.tec_name}")
        print(f"      ID   : {tec.tec_id}")


def admin_list_courses():
    title("ALL COURSES")
    print(f"\n  Total Courses: {len(lms_courses)}")
    if not lms_courses:
        info("No course has been created yet.")
    for number, course in enumerate(lms_courses, start=1):
        print(f"\n  [{number}]")
        print(f"      Course ID : {course.course_id}")
        print(f"      Course    : {course.course_name}")
        print(f"      Teacher   : {course.course_tutor.tec_name}")


def admin_remove_student():
    title("REMOVE STUDENT")
    std_id = ask("Enter Student ID")
    std = find_by(lms_std_user, "std_id", std_id)
    if std is None:
        error(f"Student with ID {std_id} does not exist.")
        return
    lms_std_user.remove(std)
    success(f"Student {std_id} has been removed successfully.")


def admin_remove_teacher():
    title("REMOVE TEACHER")
    tec_id = ask("Enter Teacher ID")
    teacher = find_by(lms_tec_user, "tec_id", tec_id)
    if teacher is None:
        error(f"Teacher with ID {tec_id} does not exist.")
        return
    lms_tec_user.remove(teacher)
    success(f"Teacher {tec_id} has been removed successfully.")


def admin_remove_course():
    title("REMOVE COURSE")
    course_id = ask("Enter Course ID")
    course = find_by(lms_courses, "course_id", course_id)
    if course is None:
        error(f"Course {course_id} does not exist.")
        return

    lms_courses.remove(course)
    if course in course.course_tutor.courses:
        course.course_tutor.courses.remove(course)
    for std in lms_std_user:
        if course in std.courses:
            std.courses.remove(course)
    success(f"Course {course_id} has been removed successfully.")


def admin_portal(admin):
    actions = {
        "2": lambda: admin_add_student(admin),
        "3": lambda: admin_add_teacher(admin),
        "4": lambda: admin_create_course(admin),
        "5": admin_list_students,
        "6": admin_list_teachers,
        "7": admin_list_courses,
        "8": admin_remove_student,
        "9": admin_remove_teacher,
        "10": admin_remove_course,
    }

    while True:
        title("ADMINISTRATION DASHBOARD")
        print(f"  Welcome, {admin.adm_name}")
        print(f"  Admin ID : {admin.adm_id}")
        print(f"  Role     : {admin.adm_profession}")
        admin_menu()
        choice = ask("Enter your choice")

        if choice == "1":
            title("ADMIN PROFILE")
            print(admin)
            pause()

        elif choice in actions:
            actions[choice]()
            pause()

        elif choice == "11":
            logout(admin.adm_name)
            break

        else:
            error("Invalid choice. Please try again.")


# ============================================================
#                         LOGIN
# ============================================================

def login(role_title, prompt, users, id_attr, portal, not_found_msg):
    title(role_title)
    user = find_by(users, id_attr, ask(prompt))
    if user is None:
        error(not_found_msg)
        pause()
    else:
        portal(user)


# ============================================================
#                       MAIN PROGRAM
# ============================================================

def main():
    load_sample_data()

    while True:
        main_header()
        role_menu()
        choice = ask("Enter your choice")

        if choice == "1":
            login("STUDENT LOGIN", "Enter your Student ID",
                  lms_std_user, "std_id", student_portal,
                  "Student ID was not found.")

        elif choice == "2":
            login("TEACHER LOGIN", "Enter your Teacher ID",
                  lms_tec_user, "tec_id", teacher_portal,
                  "Teacher ID was not found.")

        elif choice == "3":
            login("ADMINISTRATOR LOGIN", "Enter your ADMIN ID",
                  lms_admin_user, "adm_id", admin_portal,
                  "ADMIN ID was not found.")

        elif choice == "4":
            title("EXIT SYSTEM")
            print("  Thank you for using Mini LMS.")
            print("  System closed successfully.")
            break

        else:
            title("INVALID INPUT")
            error("Your input is invalid. Please select 1, 2, 3, or 4.")
            pause()

    print()
    line("═")
    print(" " * 18 + "MINI LMS CLOSED")
    print(" " * 12 + "Thank you for using the system.")
    line("═")


if __name__ == "__main__":
    main()
