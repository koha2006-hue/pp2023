#dictionary storing students and courses details
students={}
courses={}
#functions to input student details:
def student_input(): #if student_num is not integer or less than 0, return error message
    student_num=input("Enter the number of students: ")
    if not student_num.isdigit():
        print ("The number of students must be positive integer!")
        student_input()
    elif int(student_num) == 0:
        return
    elif student_num.isdigit():
        student_num=int(student_num)
        for i in range(student_num):
            student_id=input("Enter the id of student: ")
            student_name=input("Enter the name of student:")
            student_DoB=input("Enter the date of birth of student(DD/MM/YY):")
            students[student_id]={'name':student_name, 'DoB':student_DoB, 'mark':{}}
#function to input course details:
def course_input():
    course_num=input("Enter the number of courses: ")
    if not course_num.isdigit():
        print ("The number of courses must be positive integer!")
        course_input()
    elif int(course_num) == 0:
        return
    elif course_num.isdigit():
        course_num=int(course_num)
        for i in range(course_num):
            course_id=input("Enter the id of course: ")
            course_name=input("Enter the name of course:")
            courses[course_id]={'name':course_name, 'students':{}}
#function to input mark for student in selected course:
def mark_input():
    course_list()
    if len(courses)==0:
        print("No course found")
        return
    course_id=input("Enter the course id to enter the mark: ")
    if course_id not in courses:
        print("Course id not found")
        return
    for student_id in students:
        mark=float(input("Enter"+ course_id+ "mark of ID " + student_id + ":"))
        students[student_id]['mark'][course_id]= mark
        courses[course_id]['students'][student_id]=mark
#function to list all courses:
def course_list():
    if len(courses)==0:
        print("No course found")
        return
    print("The list of courses: ")
    for course_id in courses:
        course_name= courses[course_id]['name']
        print(course_id, course_name)
#function to list all students:
def student_list():
    if len(students)==0:
        print("No student found")
        return
    print("The list of students: ")     
    for student_id in students:
        student_name= students[student_id]['name']
        student_DoB= students[student_id]['DoB']
        print (student_id, student_name, student_DoB)
#function to show student marks for a given course:
def show_marks():
    course_list()
    if len(courses)==0:
        print("No course found")
        return
    course_id=input("Enter course id: ")
    if course_id not in courses:
        print ("Course id not found")
        return
    if len(courses[course_id]['students'])==0:
        print("No student found")
        return
    print("Student marks of" + course_id + ": ")
    for student_id in courses[course_id]['students']:
        mark= courses[course_id]['students'][student_id]
        print(student_id, students[student_id]['name'], mark)
#The Menu:
while True:
    print("Choose an option: ")
    print("1.Input student information: ")
    print("2.Input course information: ")  
    print("3.Input mark of given course: ")
    print("4.List courses: ")
    print("5.List students: ")
    print("6.Show student marks of a given course:")
    print("7.Exit")
    choice= input(">>>")
    if choice== "1":
        student_input()
    elif choice=="2":
        course_input()
    elif choice=="3":
        mark_input()
    elif choice=="4":
        course_list()
    elif choice=="5":
        student_list()
    elif choice=="6":
        show_marks()
    elif choice=="7":
        break
    else: 
        print("Invalid option")
    
    