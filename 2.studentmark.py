class Student:  # Student information
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
        self.marks = {}

class Course:   # Course information
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = {}

class Manager:  # Student and course management system
    def __init__(self):
        self.students = {}
        self.courses = {}

    def input_students(self):
        student_num = int(input("Enter the number of students: "))
        for i in range(student_num):
            id = input("Enter the id of student: ")
            name = input("Enter the name of student:")
            DoB = input("Enter the date of birth of student(DD/MM/YY):")
            self.students[id] = Student(id, name, DoB)

    def input_courses(self):
        course_num = int(input("Enter the number of courses: "))
        for i in range(course_num):
            id = input("Enter the id of course: ")
            name = input("Enter the name of course:")
            self.courses[id] = Course(id, name)

    def input_marks(self):
        self.list_courses()
        course_id = input("Enter the course id to enter the mark: ")
        if course_id not in self.courses:
            print("Course id not found")
            return
        for student_id in self.students:
            mark = float(input(f"Enter {course_id} mark of ID {student_id}:"))
            self.students[student_id].marks[course_id] = mark
            self.courses[course_id].students[student_id] = mark

    def list_courses(self):
        if not self.courses:
            print("No course found")
            return
        print("The list of courses: ")
        for course_id, course in self.courses.items():
            print(course_id, course.name)

    def list_students(self):
        if not self.students:
            print("No student found")
            return
        print("The list of students: ")
        for student_id, student in self.students.items():
            print(student_id, student.name, student.DoB)

    def show_marks(self):
        self.list_courses()
        if not self.courses:
            return
        course_id = input("Enter course id: ")
        if course_id not in self.courses:
            print("Course id not found")
            return
        if not self.courses[course_id].students:
            print("No student found")
            return
        print(f"Student marks of {course_id}: ")
        for student_id, mark in self.courses[course_id].students.items():
            student = self.students[student_id]
            print(student_id, student.name, mark)
#Menu:
    def menu(self):
        while True:
            print("Choose an option: ")
            print("1. Input student information")
            print("2. Input course information")
            print("3. Input mark of given course")
            print("4. List courses")
            print("5. List students")
            print("6. Show student marks of a given course")
            print("7. Exit")
            choice = input(">>> ")
            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_courses()
            elif choice == "5":
                self.list_students()
            elif choice == "6":
                self.show_marks()
            elif choice == "7":
                break
            else:
                print("Invalid option")
manage = Manager()
manage.menu()
