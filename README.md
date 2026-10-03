# 🎓 Mini LMS

A beginner-level **console-based Learning Management System** built in Python using Object-Oriented Programming (OOP). Students, teachers, and administrators each get their own menu to manage courses, assignments, and results.

Built with pure Python. No extra libraries needed.

---

## What Can It Do?

| Role | What they can do |
|------|------------------|
| **Student** | Enroll in courses, submit assignments, view results and grades |
| **Teacher** | Create assignments, view submissions, assign marks |
| **Administrator** | Add or remove students, teachers, and courses |

---

## Quick Start

**1. Make sure Python 3.6 or newer is installed**

```bash
python --version
```

**2. Download the project**

```bash
git clone https://github.com/your-username/mini-lms.git
cd mini-lms
```

**3. Run it**

```bash
python mini_lms.py
```

Use `python3 mini_lms.py` if `python` does not work on your computer.

> Your terminal should support Unicode so the boxes display correctly.

---

## Try It Out

The program comes with sample data. Log in using only the ID (no password).

| Role | ID to use |
|------|-----------|
| Student | `2025-RIS-1` |
| Teacher | `jawad342_EM_1` (teaches 3 courses) |
| Admin (can add students) | `ADM001` |
| Admin (can add teachers and courses) | `ADM002` |

### A simple walkthrough

1. Log in as a **Student** (`2025-RIS-1`) and enroll in course `EM235b`
2. Log in as a **Teacher** (`jawad342_EM_1`) and create an assignment for `EM235b`
3. Log in as the **Student** again and submit the assignment
4. Log in as the **Teacher** and choose "Assign Marks"
5. Log in as the **Student** and choose "View My Result" to see the percentage and grade

---

## Features

### 👨‍🎓 Student

- View profile
- View available (not-yet-enrolled) courses
- Enroll in a course by course ID (duplicate enrollment is blocked)
- View enrolled courses and their assignments
- Submit an assignment (each assignment can be submitted only once)
- View result: marks obtained, percentage, and letter grade

### 👨‍🏫 Teacher

- View profile and assigned courses
- View assignments for an assigned course
- Create an assignment (total marks must be greater than zero)
- View student submissions for their courses
- Assign marks (must be between 0 and the assignment's total marks)
- View a specific student's results in their courses

### 🛠️ Administrator

- View admin profile
- Add a student, add a teacher, create a course (assigning a teacher in the same step)
- View all students, teachers, and courses
- Remove a student, teacher, or course

When a course is removed, it is also removed from its teacher's list and from every student's enrolled courses.

---

## Administrator Permissions

Admin actions depend on the admin's profession.

| Action | Who can do it |
|--------|---------------|
| Add student | Admission Manager |
| Add teacher | Academic Coordinator |
| Create course | Academic Coordinator |
| View or remove anything | Any administrator |

---

## Grading Scale

| Percentage | Grade |
|:----------:|:-----:|
| 90 and above | A |
| 80 – 89 | A- |
| 70 – 79 | B+ |
| 65 – 69 | B |
| 60 – 64 | C |
| 55 – 59 | D |
| Below 55 | F |

---

## All Sample Accounts

<details>
<summary>Click to see every sample account and course</summary>

**Students**

| Name | ID |
|------|----|
| Inam | `2025-RIS-1` |
| Ali | `2025-RIS-2` |
| Zaid | `2025-RIS-3` |
| Iqra Iqbal | `2025-RIS-4` |
| Bisma Batool | `2025-RIS-5` |

**Teachers**

| Name | ID | Courses |
|------|----|---------|
| Dr. Shaid | `shaid231_AP_1` | Applied Physics |
| Dr. Ali | `ali342_AC_1` | Applied Chemistry |
| Dr. Jawad Siddiqui | `jawad342_EM_1` | Engineering Mechanics, Graphics and Designing, Robotics Vision |
| Ms. Sara Akhtar | `sara383_GD_1` | None |
| Mr. Ahmad Siddique | `ahmad235_RC_1` | None |

**Courses**

| Course ID | Course Name | Teacher |
|-----------|-------------|---------|
| `AP101q` | Applied Physics | Dr. Shaid |
| `AC1039` | Applied Chemistry | Dr. Ali |
| `EM235b` | Engineering Mechanics | Dr. Jawad Siddiqui |
| `GD355a` | Graphics and Designing | Dr. Jawad Siddiqui |
| `Robotics78c` | Robotics Vision | Dr. Jawad Siddiqui |

**Administrators**

| Name | ID | Profession |
|------|----|------------|
| Mustafa Kamal | `ADM001` | Admission Manager |
| Khizar Hayat | `ADM002` | Academic Coordinator |
| Mehmood-ul-Hassan | `ADM003` | Result Manager |
| Aqib Hussain | `ADM004` | Clerk |
| Thaira Noreen | `ADM005` | Examination Officer |

</details>

---

## How It Works

The program starts with a role menu: Student, Teacher, Administrator, or Exit. After you enter a valid ID, you reach the menu for that role and choose actions by number. Logout returns you to the role menu, so you can log in as someone else. Exit closes the program.

---

## Project Structure

```
mini-lms/
├── mini_lms.py   # The whole application
└── README.md     # This file
```

Inside `mini_lms.py`, the code is arranged in this order:

1. Configuration
2. Interface helper functions
3. Model classes
4. In-memory database and sample data
5. Student portal
6. Teacher portal
7. Admin portal
8. Login function
9. `main()` function

### Classes

| Class | Responsibility |
|-------|----------------|
| `Student` | Stores student info, enrolled courses, and submissions. Handles enrolling, submitting, and viewing results. |
| `Teacher` | Stores teacher info and assigned courses. Handles creating assignments and assigning marks. |
| `Course` | Stores course info, its teacher (`course_tutor`), and its assignments. |
| `Assignment` | Stores ID, title, total marks, and its course. |
| `AssignmentSubmission` | Links a student to an assignment and stores the marks obtained. |
| `Admin` | Stores admin info and profession, which decides what the admin may do. |

### Object relationships

```
Student   → enrolls in →  Course
Teacher   → teaches    →  Course
Teacher   → creates    →  Assignment
Student   → submits    →  Assignment (as an AssignmentSubmission)
Teacher   → assigns marks to → AssignmentSubmission
```

---

## Python Concepts Practiced

- Classes, objects, constructors (`__init__`), and the `__str__` method
- Object relationships (objects storing references to other objects)
- Lists of custom objects with `.append()` and `.remove()`
- Functions to split the program into reusable parts
- Loops and conditionals for menus, permissions, and grading
- `input()` handling and `int()` conversion with `try` / `except ValueError`
- Basic validation (marks range, duplicate IDs, duplicate submissions)
- A search helper using `getattr()` and `next()` with a generator expression
- A generator function (`yield`) for a teacher's submissions
- A dictionary of functions (with `lambda`) for admin menu actions
- The `if __name__ == "__main__":` entry point

---

## Current Limitations

- **No saved data:** everything is kept in memory and resets when the program closes
- **No passwords:** login uses an existing ID only, and IDs are case-sensitive
- **Limited validation:** names, emails, and IDs are accepted as typed
- **No editing:** records and assignments can only be added or removed
- **Assign Marks** prompts for every submission each time, including ones already graded
- **Removing a teacher** does not remove or reassign their courses

---

## Future Improvements

- Save data to a file or database
- Password-based login
- Editing for users, courses, and assignments
- Stronger input validation
- A graphical or web interface

---

## Learning Purpose

This project was built to practice core Python and OOP concepts (classes, objects, relationships, functions, loops, conditionals, and lists of custom objects) in one connected system instead of small standalone scripts.

---

## Author

**Inamelahi**
BS Robotics and Intelligent Systems student
