# Mini LMS

## 📌 About the Project

Mini LMS is a beginner-level **console-based Learning Management System** built in Python using Object-Oriented Programming (OOP). It simulates three types of users — Students, Teachers, and Admins — who interact with courses, assignments, and results through a simple text-based menu system.

This project was built as a practical exercise to apply core Python and OOP concepts in a single connected system, rather than isolated small scripts.

## ✨ Features

- Role-based access: Student, Teacher, and Admin each get their own menu
- Course enrollment for students
- Assignment creation by teachers
- Assignment submission by students
- Marks assignment and automatic grade calculation
- Admin-level management of students, teachers, and courses
- All interaction happens through the terminal using numbered menu choices

## 👥 User Roles

### Student

- View student profile
- View available (not-yet-enrolled) courses
- Enroll in a course by course ID
- View enrolled courses
- View assignments for an enrolled course
- Submit an assignment
- View result (total marks obtained, percentage, and letter grade)
- Logout

### Teacher

- View teacher profile
- View assigned courses
- View assignments for an assigned course
- Create a new assignment for an assigned course
- View student submissions for their courses
- Assign marks to a student's submission
- View a specific student's results for their course
- Logout

### Admin

Admin actions are permission-based — each admin has a specific profession, and only certain professions can perform certain actions:

- View admin profile
- Add a student *(requires "Admission Manager" profession)*
- Add a teacher *(requires "Academic Coordinator" profession)*
- Create a course and assign a teacher to it in the same step *(requires "Academic Coordinator" profession)*
- View all students
- View all teachers
- View all courses
- Remove a student
- Remove a teacher
- Remove a course
- Logout

## 🧠 Python Concepts Practiced

This project was built to practice:

- Classes and objects (`Student`, `Teacher`, `Course`, `Assignment`, `AssignmentSubmission`, `Admin`)
- Constructors (`__init__`) and instance attributes
- Instance methods (e.g. `student_enroll()`, `create_assignment()`, `assign_marks()`)
- The `__str__` method for readable object printing
- Lists for storing collections of objects (students, teachers, courses, assignments, submissions)
- Loops (`for`, `while`) for menus and searching through lists
- Conditional statements (`if` / `elif` / `else`) for menu logic, permission checks, and grade calculation
- Object relationships — objects storing references to other objects (e.g. a `Course` stores its `Teacher`, an `AssignmentSubmission` stores its `Assignment`)
- Input handling with `input()` and basic type conversion (`int()`)
- Basic validation (e.g. checking that assigned marks don't exceed the total, checking whether an ID already exists before adding a new user)
- Searching through lists using loops to find a matching ID
- Adding and removing objects from lists (`.append()`, `.remove()`)

## 🏗️ Project Structure / Classes

| Class | Responsibility |
|---|---|
| `Student` | Stores student info, enrolled courses, and submissions. Handles enrolling, submitting assignments, and viewing results. |
| `Teacher` | Stores teacher info and assigned courses. Handles creating assignments and assigning marks. |
| `Course` | Stores course info, its assigned teacher (`course_tutor`), and its list of assignments. |
| `Assignment` | Stores assignment info (ID, title, total marks) and which course it belongs to. |
| `AssignmentSubmission` | Represents a student's submission of a specific assignment, and the marks obtained. |
| `Admin` | Stores admin info and profession, which determines what actions they're allowed to perform. |

**Object relationships:**

```
Student   → enrolls in →  Course
Teacher   → teaches    →  Course
Teacher   → creates    →  Assignment
Student   → submits    →  Assignment (as an AssignmentSubmission)
Teacher   → assigns marks to → AssignmentSubmission
```

## ▶️ How to Run

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code (or any editor/terminal).
4. Open a terminal in that folder and run:

   ```bash
   python mini_lms.py
   ```

5. Follow the on-screen prompts to select a role and log in using one of the sample IDs below.

**Sample IDs to try (from the built-in demo data):**

| Role | Sample ID |
|---|---|
| Student | `2025-RIS-1` |
| Teacher | `shaid231_AP_1` |
| Admin | `ADM002` (Academic Coordinator — can add teachers/courses) |
| Admin | `ADM001` (Admission Manager — can add students) |

## 🖥️ How the Program Works

When the program starts, it asks you to choose a role: Student, Teacher, or Admin. After entering a valid ID for that role, you're taken into a menu specific to that role, where you enter a number to choose an action. The menu keeps repeating until you choose the logout option. Each role's menu only shows actions relevant to that role, and admin actions are further restricted based on the admin's profession.

## ⚠️ Current Limitations

- **No persistent storage** — all data (students, courses, enrollments, submissions, grades) is held only in memory using Python lists. Once the program is closed, everything resets back to the original sample data the next time it runs.
- **Single session only** — the program only asks for a role once at the start; you can't switch roles without restarting the program.
- **Minimal input validation** — most inputs (IDs, names, emails) are accepted as typed, with only a few checks in place (such as marks not exceeding the assignment total, or an ID already existing).
- **No authentication/passwords** — logging in only requires entering an existing ID, with no password protection.

## 🚀 Future Improvements

These are ideas for later, not features that currently exist:

- Persistent data storage (e.g. saving to a file) so data survives between runs
- Stronger input validation across all menus
- A graphical or web-based interface instead of the terminal
- Basic authentication (passwords) for logging in

## 🎯 Learning Purpose

This project was built as a hands-on way to practice and strengthen core Python and Object-Oriented Programming concepts — including classes, objects, relationships between objects, loops, conditionals, and working with lists of custom objects — by building something more connected and realistic than small standalone exercises.

## 👨‍💻 Author

**Inamelahi**
BS Robotics and Intelligent Systems student
