class Student:          #student information
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:           #course information
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = {}

class Manage_system:    #Manage students system
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self):
        id = input("Enter the id of the student: ")
        name = input("Enter the name of the student: ")
        dob = input("Enter the date of birth of the student: ")
        student = Student(id, name, dob)
        self.students[id] = student

    def add_course(self):
        id = input("Enter the id of the course: ")
        name = input("Enter the name of the course: ")
        course = Course(id, name)
        self.courses[id] = course

    def add_mark(self):
        course_id = input("Enter the id of the course: ")
        if course_id not in self.courses:
            print("Course id not found")
            return
        for student_id in self.students:
            mark = input(f"Enter the mark of ID {student_id} in this course: ")
            self.students[student_id].marks[course_id] = mark
            self.courses[course_id].students[student_id] = mark

    def list_courses(self):
        print("The list of courses: ")
        for course_id in self.courses:
            course_name = self.courses[course_id].name
            print(course_id, course_name)

    def list_students(self):
        print("The list of students: ")
        for student_id in self.students:
            student_name = self.students[student_id].name
            print(student_id, student_name)

    def show_marks(self):
        course_id = input("Enter course id: ")
        if course_id not in self.courses:
            print("Course id not found")
            return
        print(f"Student marks of {course_id}: ")
        for student_id in self.courses[course_id].students:
            mark = self.courses[course_id].students[student_id]
            student_name = self.students[student_id].name
            print(student_id, student_name, mark)

#Menu
manager = Manage_system()
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
        manager.add_student()
    elif choice == "2":
        manager.add_course()
    elif choice == "3":
        manager.add_mark()
    elif choice == "4":
        manager.list_courses()
    elif choice == "5":
        manager.list_students()
    elif choice == "6":
        manager.show_marks()
    elif choice == "7":
        break
    else: 
        print("Invalid option")
