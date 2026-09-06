#######   Mini Lms
class Student:
    def __init__(self,std_name,std_id,std_email):
           self.std_name = std_name
           self.std_id = std_id
           self.std_email = std_email
           self.courses = []
           self.submission = []

    def __str__(self):
          return f"Student name = {self.std_name}\nStudent ID = {self.std_id}"

    def student_enroll(self,course):
          self.courses.append(course)
    def submit_assignment(self,assignment,course):
         
         if course in self.courses:
                if assignment in course.assignments:
                      submission_1 = AssignmentSubmission(self.std_id,assignment)
                      self.submission.append(submission_1)
                else:
                       print("This is not your assigned assignment")

    def check_grade(self,percentage,course):
          if percentage >= 90:
                print(f"{self.std_name} got A grade in {course.course_name}")
          elif percentage >= 80:
                print(f"{self.std_name} got A- grade in {course.course_name}") 
          elif percentage >= 70:
                print(f"{self.std_name} got B+ grade in {course.course_name}")
          elif percentage >= 65:
                print(f"{self.std_name} got B grade in {course.course_name}")  
          elif percentage >= 60:
                print(f"{self.std_name} got C grade in {course.course_name}")
          elif percentage >= 55:
                print(f"{self.std_name} got D grade in {course.course_name}")
          else:
                print(f"{self.std_name} got F grade")
                print(f"{self.std_name} has been failed in this course in {course.course_name}")
          

    def view_result(self,course):
             percentage = 0
             std_result = False
             if course not in  self.courses:
                   print("You are not enrolled in this course")
             else:
                   
                   total_marks = 0
                   get_marks = 0
                   if course.assignments:
                        if self.submission:
                              for assignment in course.assignments:
                                    total_marks += assignment.assignment_marks
                                          
                                    for submission in self.submission:
                                                      
                                          if submission.assignment == assignment:
                                                if submission.obtained_marks is not None:
                                                       get_marks += submission.obtained_marks
                                                       std_result = True
                                                            
                        else:
                               print(f"{self.std_name} has not submitted any assignment")
                   else:
                         print(f"{course.course_name} has no assignment yet")
             if std_result == True:
                   percentage = (get_marks * 100) / total_marks
                   print(f"You have got {get_marks} from {total_marks} ")
                   print(f"your marks Percentage = {percentage:.2f}%")
                   self.check_grade(percentage,course)

                  

                               

class Teacher:
      def __init__(self,tec_name,tec_id):
            self.tec_name = tec_name
            self.tec_id = tec_id
            self.courses = []
            self.submitted_assignment = []
            self.created_assignment  =  []

      def __str__(self):
            return f"Teacher name = {self.tec_name }\nTeacher ID = {self.tec_id}"


      def add_course(self,course):
            self.courses.append(course)

      def create_assignment(self,course,assignment_id,assignment_title,assignment_marks):
            assignment_1 = Assignment(course,assignment_id,assignment_title,assignment_marks)
            course.assignments.append(assignment_1)
            self.created_assignment.append(assignment_1)
            
      def assign_marks(self,submission,marks):
            if self.tec_id == submission.assignment.course.course_tutor.tec_id:
                 total_marks = submission.assignment.assignment_marks
                 if marks < 0 or marks > total_marks:
                      print("Invalid marks have been assigned")
                 else:
                      submission.obtained_marks = marks
            else:
                  print("Your input is invalid")
            

class Course:
      def __init__(self,course_name,course_id,course_tutor):
            self.course_name = course_name
            self.course_id = course_id
            self.course_tutor = course_tutor
            self.assignments = []

      def __str__(self):
           return f"Course ID: {self.course_id} | Course: {self.course_name}"

class Assignment():
      def __init__(self,course,assignment_id,assignment_title,assignment_marks):
            self.course = course
            self.assignment_id = assignment_id
            self.assignment_title = assignment_title
            self.assignment_marks = assignment_marks

class AssignmentSubmission:
      def __init__(self,std_id,assignment):
            self.std_id = std_id
            self.assignment = assignment
            self.obtained_marks = None

class Admin:
      def __init__(self,adm_name,adm_id,adm_gmail,adm_profession):
            self.adm_name = adm_name
            self.adm_id = adm_id
            self.adm_gmail = adm_gmail
            self.adm_profession = adm_profession
      def __str__(self):
            return f"Name : {self.adm_name}\nProfession : {self.adm_profession}"

lms_std_user = []
lms_tec_user = []
lms_admin_user = []
lms_courses = []
     
#students object

std_1 =  Student("inam","2025-RIS-1","inamelahi243@gmail.com")  
std_2 = Student("ali","2025-RIS-2","ali243@gmail.com")
std_3 = Student("Zaid","2025-RIS-3","zaid456@gmail.com")
std_4 = Student("Iqra Iqbal","2025-RIS-4","zaid456@gmail.com")
std_5 = Student("Bisma Batool","2025-RIS-5","zaid456@gmail.com")

#teacher objects
tec_1 = Teacher("Dr.Shaid","shaid231_AP_1") 
tec_2 = Teacher("Dr.Ali","ali342_AC_1")  
tec_3 = Teacher("Dr.jawad siddiqui","jawad342_EM_1")
tec_4 = Teacher("Ms.Sara Akhtar","sara383_GD_1")
tec_5 = Teacher("Mr.Ahmad siddique","ahmad235_RC_1")
#class objects
crs_1 = Course("Applied Physic","AP101q",tec_1)
crs_2 = Course("Applied Chemisty","AP C1039",tec_2)
crs_3 = Course("Engineering Mechanics","EM 235b",tec_3)
crs_4 = Course("Graphics and Designing","GD355a",tec_3)
crs_5 = Course("Robotics_vision","Robotics78c",tec_3)

tec_1.add_course(crs_1)
tec_2.add_course(crs_2)
tec_3.add_course(crs_3)
tec_3.add_course(crs_4)
tec_3.add_course(crs_5)

adm_1 = Admin("Mustafa kamal","ADM001","mustafa123@gmail.com","Admission Manager")
adm_2 = Admin("khizar Hayat","ADM002","Khizar123@gmail.com","Academic Coordinator")
adm_3 = Admin("Mehmood-ul-hassan","ADM003","mehmood131@gmail.com","Result Manager")
adm_4 = Admin("Aqib Hussain","ADM004","aqib127@gmail.com","Clerk")
adm_5 = Admin("Thaira noreen","ADM005","noreen123@gmail.com","Examination officer")

lms_admin_user.append(adm_1)
lms_admin_user.append(adm_2)
lms_admin_user.append(adm_3)
lms_admin_user.append(adm_4)
lms_admin_user.append(adm_5)


lms_courses.append(crs_1)
lms_courses.append(crs_2)
lms_courses.append(crs_3)
lms_courses.append(crs_4)
lms_courses.append(crs_5)

lms_std_user.append(std_1)
lms_std_user.append(std_2)
lms_std_user.append(std_3)
lms_std_user.append(std_4)
lms_std_user.append(std_5)
lms_tec_user.append(tec_1)
lms_tec_user.append(tec_2)
lms_tec_user.append(tec_3)
lms_tec_user.append(tec_4)
lms_tec_user.append(tec_5)

print("******* ====== ******** ====== *****")
print("******* ====== ******** ====== *****")
print("***     ====== Mini LMS ======   ***")
print("******* ====== ******** ====== ******")
print("******* ====== ******** ====== *****")

print("Enter your status:\n1:Student\n2:Teacher\n3:Admin ")
user_choice = input("Enter your choice:")
found = False
if user_choice == "1":
      user_id = input("Enter your Student ID : ")
      for user in lms_std_user:
            if user.std_id == user_id:
                  found = True
                  break
      if found == False:
            
            print("STUDENT ID is not found ")
      else: 
        while True:
                  print(f"Welcome : {user.std_name}")
                  print("====== ====== ====== ======")
                  print("====== STUDENT MENU ======")
                  print("====== ====== ====== ======")
                  print("""
                        1: View My Profile
                        2: View Available Courses
                        3: Enroll in Course
                        4: View My Courses
                        5: View Course Assignments
                        6: Submit Assignments
                        7: View My result
                        8: Logout""")
                  choice = input("Enter your choice: ")
                  if choice == "1":
                        print(user)
                  elif choice == "2":
                        for course in lms_courses:
                              if course not in user.courses:
                                    print(course)
                                    print("\n")
                  elif choice == "3":
                        enroll_crs_id = input("Enter the course ID :")
                        course_found = False
                        for course in lms_courses:
                        
                              if enroll_crs_id == course.course_id:
                                          course_found = True
                                          if course in user.courses:
                                              print(f"You have already enrolled in this course = {course.course_name}")
                                              break
                                          else:
                                              print(f"Course Name : {course}")
                                              user.student_enroll(course)
                                              print(f"You have enrolled now in {course.course_name}")
                                              break
                        
                        if course_found == False:
                              print(f"{enroll_crs_id} course ID is not Found")
                  elif choice == "4":
                        
                        if user.courses:
                              for course in user.courses:
                                    print(f"you have enrolled in {course.course_name} " )
                        else:
                              print("You are not enrolled in any course")
                  elif choice == "5":
                        course_id = input("Enter the course ID : ")
                        course_found = False
                        for course in user.courses:
                              if course_id == course.course_id:
                                    course_found = True
                                    if course_found:
                                          print(course.course_name)
                                          if course.assignments:
                                                for assignment in course.assignments:
                                                      print(assignment)
                                                break
                                          else:
                                                print(f"{course.course_name} has no assignments")
                        if course_found == False:
                                   print("You are not enrolled by this course_id")
                  elif choice == "6":
                        course_id = input("Enter the course_id:")
                        course_found = False
                        assignment_found = False
                        for course in user.courses:
                              if course_id == course.course_id:
                                    print(f"Yes,you are enrolled in {course.course_name}")
                                    course_found = True
                                    sbmt_assign_id = input("Enter your assignment ID:")
                                    if course.assignments:
                                         for assignment in course.assignments:
                                               if sbmt_assign_id == assignment.assignment_id:
                                                     print("Your assignment has been submitted")
                                                     assignment_found = True
                                                     user.submit_assignment(assignment,course)
                                                     break
                                                     
                                         if assignment_found == False:
                                                print(f"There is no uploaded assignment by this id")
                                    else:
                                          print("This course has no assignments")
                        if course_found == False:
                              print(f"You are not enrolled in any course by this {course_id}")
                  elif choice == "7":
                        course_id = input("Enter the course id:")
                        for course in user.courses:
                              if course_id == course.course_id:
                                    user.view_result(course)
                                    break
                        
                       
                  elif choice == "8":
                        print(f"Goodbye {user.std_name}!")
                        break
                                                                              
            
elif user_choice == "2":
      user_id = input("Enter your Teacher ID : ")
      for user in lms_tec_user:
            if user.tec_id == user_id:
                  found = True
                  break
      if found == False:
            print("TEACHER ID is not found")
      if found:
            while True:
                  print(f"Welcome : {user.tec_name}SB")
                  print("====== ====== ====== ======")
                  print("====== TEACHER MENU ======")
                  print("====== ====== ====== ======")
                  print("""
                        1: View My Profile
                        2: View My Courses
                        3: View Courses Assignments
                        4: Create Assignment
                        5: View Student Submissions
                        6: Assign Marks
                        7: View Student Results
                        8: Logout""")

                  user_choice = input("Enter your choice:")
                  if user_choice == "1":
                        print(user)
                  elif user_choice == "2":
                        if user.courses:
                              print("Your's courses are below here:")
                              for course in user.courses:
                                    print(f"{course.course_name}")
                        else:
                              print("You have no course yet")
                  elif user_choice == "3":
                        course_id = input("Enter your course ID:")
                        course_found = False
                        if user.courses:
                              for course in user.courses:
                                    if course_id == course.course_id:
                                          course_found = True
                                          print(f"Verified,this course : {course.course_name} is assigned to you")
                                          print("Course Assignments")
                                          if course.assignments:
                                                for assignment in course.assignments:
                                                      print(assignment)
                                                
                                          else:
                                                print(f"You have not created any assignment for this course")
                                          break
                              if course_found == False:
                                    print(f"This course ID is not matching for your assigned courses")
                        else:
                              print(f"{user.tec_name}\nStill there is no course assigned to you by admin")
                  elif user_choice == "4":
                        course_id = input("Enter the course_ID:")
                        found_course = False
                        for course in user.courses:
                              if course_id == course.course_id:
                                    found_course = True
                                    print(f"Course name : {course.course_name}")
                                    assignment_id = input("Enter the assignment ID:")
                                    assignment_title = input("Enter the assignment title:")
                                    assignment_marks = int(input("Enter the assignment marks:"))
                                    user.create_assignment(course,assignment_id,assignment_title,assignment_marks)
                                    break
                        if found_course == False:
                              print(f"ID : {course_id} is not assigned to you\nYou cannot create assignment for this course")
  
                  elif user_choice == "5":
                        no_of_submission = 0
                        for std in lms_std_user:
                              for submission in std.submission:
                                    course_name = submission.assignment.course.course_name
                                    teacher = submission.assignment.course.course_tutor
                                    if teacher == user:
                                          print(f"{std.std_name} has been submitted = {submission.assignment.assignment_title}\nof this course: {course_name}")
                                          no_of_submission += 1

                        print(f"Total Submission = {no_of_submission}")
                  elif user_choice == "6":
                        for std in lms_std_user:
                              for submission in std.submission:
                                    course_name = submission.assignment.course.course_name
                                    teacher = submission.assignment.course.course_tutor
                                    if teacher == user:
                                          marks = submission.assignment.assignment_marks
                                          print(f"Student: {std.std_name}")
                                          print(f"Assignment: {submission.assignment.assignment_title}")
                                          print(f"Total marks: {submission.assignment.assignment_marks}")
                                          assigned_marks = int(input("How many marks you want to give this student"))
                                          user.assign_marks(submission,assigned_marks)
                  elif user_choice == "7":
                        student_id = input("Enter your Student ID:")
                        std_id_found = False
                        for std in lms_std_user:
                              if std.std_id == student_id:
                                    std_id_found = True
                                    if std.submission:
                                          for submission in std.submission:
                                                if submission.assignment.course.course_tutor == user:
                                                      print(f"Student name : {std.std_name}")
                                                      print(f"Course name : {submission.assignment.course.course_name}")
                                                      print(f"Assignment title : {submission.assignment.assignment_title}")
                                                      print(f"Total marks : {submission.assignment.assignment_marks}")
                                                      print(f"Obtained marks : {submission.obtained_marks}")

                                    else:
                                          print(f"{std.std_name} has not submitted any assignment for this course")
                        if std_id_found == False:
                              print(f"This id {student_id} is not matching")

                  elif user_choice == "8":
                        print("Thankyou,stay connected")
                        break
                                    

elif user_choice == "3":
      user_id = input("Enter your ADMIN ID :")

      for user in lms_admin_user:
            if user.adm_id == user_id:
                  found = True
                  break
      
      if found == False: 
            print("ADMIN ID is not found")
      else:
            while True:
                  print(f"Welcome : {user.adm_name}")
                  print("====== ====== ====== ======")
                  print("====== ADMIN MENU ======")
                  print("====== ====== ====== ======")
                  print("""
                        1: View Admin Profile
                        2: Add Student
                        3: Add Teacher
                        4: Create Course
                        5: View All Students
                        6: View All Teachers
                        7: View All Courses
                        8: Remove Student
                        9: Remove Teacher
                        10: Remove Course
                        11: Logout""")
                  user_choice = input("Enter your choice:")
                  if user_choice == "1":
                        print(user)
                  elif user_choice == "2":
                        if user.adm_profession == "Admission Manager":
                              
                              std_id = input("Enter the student ID:")
                              std_exist = False
                              for std in lms_std_user:
                                    if std.std_id == std_id:
                                          std_exist = True
                                          print(f"Student is already admitted by this {std_id} ")
                              if std_exist == False:
                                    std_gmail = input("Enter the student gmail:")
                                    std_name = input("Enter the student name:")
                                    std = Student(std_name,std_id,std_gmail)
                                    lms_std_user.append(std)    
                        else:
                              print("You are not authorized to add Student")
                  
                  elif user_choice == "3":
                        if user.adm_profession == "Academic Coordinator":
                              teacher_id = input("Enter the teacher ID:")
                              tec_exist = False
                              for tec in lms_tec_user:
                                    if teacher_id == tec.tec_id:
                                          tec_exist = True
                                          print(f"Teacher is already admitted  by this id {teacher_id}")
                                          break     
                              if tec_exist == False:
                                    teacher_name = input("Enter the teacher name:")
                                    tec = Teacher(teacher_name,teacher_id)
                                    lms_tec_user.append(tec)
                                    
                        else:
                              print("You are not authorized to add teacher")

                  elif user_choice == "4":
                        if user.adm_profession == "Academic Coordinator":
                              course_exist = False
                              course_id = input("Enter the course ID:")
                              for course in lms_courses:
                                    if course_id == course.course_id:
                                          course_exist = True
                                          print(f"The course has already been created with this ID {course_id}")
                                          break
                              if course_exist == False:
                                    course_name = input("Enter the course name :")
                                    tutor_id = input("Enter the course tutor:")
                                    course_id = input("Enter the course ID:")
                                    teacher_found = False
                                    for tutor in lms_tec_user:
                                          if tutor.tec_id == tutor_id:
                                                teacher_found = True
                                                course = Course(course_name,course_id,tutor)
                                                lms_courses.append(course)
                                                tutor.add_course(course)
                                                break
                                    if teacher_found == False:
                                          print(f"Invalid Teacher ID")
                        else:
                              print(f"You are not authorized to create the course")
                  elif user_choice == "5":
                        print("Number of students:", len(lms_std_user))
                        if len(lms_std_user) == 0:
                              print("No student is registered yet")
                        else:
                              for std in lms_std_user:
                                    print(std)

                  elif user_choice =="6":
                        if len(lms_tec_user) == 0:
                              print("No teacher is registered yet")
                        else:
                              for tec in lms_tec_user:
                                    print(tec)
                  elif user_choice == "7":
                        if len(lms_courses) == 0:
                              print("No course is created yet")
                        else:
                              for course in lms_courses:
                                    print(course)
                  elif user_choice == "8":
                        std_id = input("Enter the Student ID: ")
                        student_found = False
                        for std in lms_std_user:
                              if std.std_id == std_id:
                                    student_found = True
                                    lms_std_user.remove(std)
                                    print(f"Student {std_id} has been removed successfully.")
                                    break

                        if student_found == False:
                              print(f"Student with ID {std_id} does not exist.")
                  elif user_choice == "9":
                         tec_id = input("Enter the teacher ID: ")
                         teacher_found = False
                         for teacher in lms_tec_user:
                              if teacher.tec_id == tec_id:
                                    teacher_found = True
                                    lms_tec_user.remove(teacher)
                                    print(f"Teacher {tec_id} has been removed successfully.")
                                    break

                         if teacher_found == False:
                              print(f"Teacher with ID {tec_id} does not exist.")
                  elif user_choice == "10":
                         course_id = input("Enter the Course ID: ")
                         course_found = False
                         for course in lms_courses:
                              if course.course_id == course_id:
                                    course_found = True
                                    lms_courses.remove(course)
                                    print(f"Course {course_id} has been removed successfully.")
                                    break

                         if course_found == False:
                              print(f"Course with ID {course_id} does not exist.")
                  elif user_choice == "11":
                        print("Thankyou , Stay Connected")
                        break
else:
      print("Your input is invalid")
