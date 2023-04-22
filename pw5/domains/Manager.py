import curses
import math
import numpy as np
from input import input_courses, input_students, input_marks
from domains.Course import Course
from domains.Students import Student
import zipfile
stdscr = curses.initscr()
class Manager:
    def __init__(self):
        self.students = {}
        self.courses = {}
#check if students.dat exist and if yes, decompess all files to work with before start
    def start(self):
        try:
            with zipfile.ZipFile("students.dat", mode="r") as zf:
                zf.extractall()
        except:
            pass
        with open("students.txt", "r") as f:
            for line in f:
                student_id, name, DoB = line.split()
                self.students[student_id.encode()] = Student(student_id.encode(), name.encode(), DoB.encode())
        with open("courses.txt", "r") as f:
            for line in f:
                course_id, name, credit = line.split()
                self.courses[course_id.encode()] = Course(course_id.encode(), name.encode(), int(credit))
        with open("marks.txt", "r") as f:
            for line in f:
                course_id, student_id, mark = line.split()
                self.students[student_id.encode()].marks[course_id.encode()] = int(mark)
#compress all files before exit
    def exit(self):
        compression = zipfile.ZIP_DEFLATED
        zipfile_name = "students.dat"
        with zipfile.ZipFile(zipfile_name, mode="w") as zf:
            for file_name in ["students.txt", "courses.txt", "marks.txt"]:
                if file_name.endswith(".txt"):
                    zf.write(file_name, compress_type=compression)
        stdscr.addstr("All files are compressed")
        stdscr.refresh()
        stdscr.getch()
        curses.endwin()
        exit()
    def input_students(self):
        input_students(self)
    def input_courses(self):
        input_courses(self)
    def input_marks(self):
        input_marks(self)
    def reset_screen(self):
        stdscr.clear()
        self.menu()
        stdscr.refresh()
    def list_courses(self):
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        current_row= int(10)
        if not self.courses:
            stdscr.addstr("No course found")
            stdscr.refresh()
            stdscr.getch()
            return
        stdscr.addstr("The list of courses: \n", curses.color_pair(3))
        current_row += 1
        stdscr.refresh()
        for course_id, course in self.courses.items():
            stdscr.addstr(course_id.decode()+" " +course.name.decode()+ " credit: "+ str(course.credit)+"\n")
            current_row += 1
            stdscr.refresh()
        stdscr.getch()
    def list_students(self):
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        current_row= int(10)
        if not self.students:
            stdscr.addstr("No student found")
            stdscr.refresh()
            stdscr.getch()
            return
        stdscr.addstr("The list of students: \n", curses.color_pair(2))
        current_row += 1
        stdscr.refresh()
        for student_id, student in self.students.items():
            stdscr.addstr(student_id.decode()+" " +student.name.decode()+" "+ student.DoB.decode()+"\n")
            current_row += 1
            stdscr.refresh()
        stdscr.getch()
    def show_marks(self):
        self.list_courses()
        if not self.courses:
            stdscr.addstr("No course found")
            stdscr.refresh()
            stdscr.getch()
            return
        stdscr.addstr("Enter the id of course: ")
        stdscr.refresh()
        curses.echo()
        course_id = stdscr.getstr()
        y,x = stdscr.getyx()
        while course_id not in self.courses:
            stdscr.move(y,x)
            stdscr.clrtoeol()
            stdscr.addstr("Enter the valid course id: ")
            stdscr.refresh()
            curses.echo()
            course_id = stdscr.getstr()
        course = self.courses[course_id]
        self.list_students()
        if not course.students:
            stdscr.addstr("No student found")
            stdscr.refresh()
            stdscr.getch()
            return
        stdscr.addstr("Enter the id of student: ")
        stdscr.refresh()
        curses.echo()
        student_id = stdscr.getstr()
        y,x = stdscr.getyx()
        while student_id not in course.students:
            stdscr.move(y,x)
            stdscr.clrtoeol()
            stdscr.addstr("Enter the valid student id: ")
            stdscr.refresh()
            curses.echo()
            student_id = stdscr.getstr()
        student = course.students[student_id]
        stdscr.addstr(f"Mark of student {student_id} in course {course_id} is {student.marks[course_id]}")
        stdscr.refresh()
        stdscr.getch()

    def calculate_GPA(self, student_id):
        student = self.students[student_id]
        marks = np.array(list(student.marks.values()))
        marks=np.array([math.floor(mark*10)/10 for mark in marks])
        credits = np.array([self.courses[course_id].credit for course_id in student.marks])
        student.GPA = np.sum(marks*credits)/np.sum(credits)
    def calculate_all_GPA(self):
        for student_id in self.students:
            self.calculate_GPA(student_id)

    def show_GPA(self):
        if not self.students:
            stdscr.addstr("No student found")
            stdscr.refresh()
            stdscr.getch()
            return
        self.list_students()
        stdscr.addstr("Enter the id of student: ")
        stdscr.refresh()
        curses.echo()
        student_id = stdscr.getstr()
        y,x = stdscr.getyx()
        while student_id not in self.students:
            stdscr.move(y,x)
            stdscr.clrtoeol()
            stdscr.addstr("Enter the valid student id: ")
            stdscr.refresh()
            curses.echo()
            student_id = stdscr.getstr()
        self.calculate_GPA(student_id)
        stdscr.addstr(f"GPA of student {student_id} is {self.students[student_id].GPA}")
        stdscr.refresh()
        stdscr.getch()
    def show_all_GPA(self):
        if not self.students:
            stdscr.addstr("No student found")
            stdscr.refresh()
            stdscr.getch()
            return
        self.calculate_all_GPA()
        stdscr.addstr("The list of students GPA: \n")
        stdscr.refresh()
        for student_id, student in self.students.items():
            stdscr.addstr(student_id.decode()+" " +student.name.decode()+" "+ str(student.GPA)+"\n")
            stdscr.refresh()
        stdscr.getch()
    def sort_by_GPA(self):
        if not self.students:
            stdscr.addstr("No student found")
            stdscr.refresh()
            stdscr.getch()
            return
        self.calculate_all_GPA()
        stdscr.addstr("The list of students GPA: \n")
        stdscr.refresh()
        for student_id, student in sorted(self.students.items(), key=lambda x: x[1].GPA, reverse=True):
            stdscr.addstr(student_id.decode()+" " +student.name.decode()+" "+ str(student.GPA)+"\n")
            stdscr.refresh()
        stdscr.getch()
    def menu(self):
                menu=["1. Add student","2. Add course","3. Add mark","4. List students","5. List courses","6. Show marks","7. Show GPA","8. Show all GPA","9. Sort by GPA","10. Exit"+'\n']
                def print_menu(stdscr,current_row):
                    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
                    for i in range(len(menu)):
                        if i == current_row:
                            stdscr.attron(curses.color_pair(1))
                            stdscr.addstr(i,0,menu[i],curses.color_pair(1))
                            stdscr.attroff(curses.color_pair(1))
                        else:
                            stdscr.addstr(i,0,menu[i])
                    stdscr.refresh()
                def main(stdscr):
                    curses.curs_set(0)
                    current_row = 0
                    print_menu(stdscr,current_row)
                    while 1:
                        key = stdscr.getch()
                        if key == curses.KEY_UP and current_row > 0:
                            current_row -= 1
                        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
                            current_row += 1
                        elif key == curses.KEY_ENTER or key in [10,14]:
                            choice = menu[current_row]
                            if choice == "1. Add student":
                                self.input_students()
                                self.reset_screen()
                            elif choice == "2. Add course":
                                self.input_courses()
                                self.reset_screen()
                            elif choice == "3. Add mark":
                                self.input_marks()
                                self.reset_screen()
                            elif choice == "4. List students":
                                self.list_students()
                                self.reset_screen()
                            elif choice == "5. List courses":
                                self.list_courses()
                                self.reset_screen()
                            elif choice == "6. Show marks":
                                self.show_marks()
                                self.reset_screen()
                            elif choice == "7. Show GPA":
                                self.show_GPA()
                                self.reset_screen()
                            elif choice == "8. Show all GPA":
                                self.show_all_GPA()
                                self.reset_screen()
                            elif choice == "9. Sort by GPA":
                                self.sort_by_GPA()
                                self.reset_screen()
                            elif choice == "10. Exit":
                                self.exit()
                            else:
                                self.exit()
                        print_menu(stdscr,current_row)
                        stdscr.refresh()
                curses.wrapper(main)