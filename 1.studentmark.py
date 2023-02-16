#dictionary storing students and courses details
students={}
courses={}
#functions to input student details:
def student_input():
    student_num = int(input("Enter the number of students:"))
    for i in range(student_num):
        student_id=input("Enter the id of student: ")
        student_name=input("Enter the name of student: ")
        student_DoB=input ("Enter the date of student: ")
        students[student_id]={'name':student_name, 'DoB':student_DoB, 'mark':{} }
#function to input course details:
def course_input():
    course_num=int(input("Enter the number of courses: "))
    for i in range(course_num):
        course_id=input("Enter the id of course: ")
        course_name=input("Enter the name of course:")
        courses[course_id]={'name':course_name, 'students':{}}
#function to input mark for student in selected course:
def mark_input():
    course_id=input("Enter the course id: ")
    if course_id not in courses:
        print("Course id not found")
        return
    for student_id in students:
        mark=input("Enter the mark of ID " + student_id + " in this course: ")
        students[student_id]['mark'][course_id]= mark
        courses[course_id]['students'][student_id]=mark
#function to list all courses:
def course_list():
    print("The list of courses: ")
    for course_id in courses:
        course_name= courses[course_id]['name']
        print(course_id, course_name)
#function to list all students:
def student_list():
    print("The list of students: ")
    for student_id in students:
        student_name=students[student_id]['name']
        print(student_id,student_name)
#function to show student marks for a given course:
def show_marks():
    course_id=input("Enter course id: ")
    if course_id not in courses:
        print ("Course id not found")
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
    
    