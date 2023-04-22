import curses
import re
from domains.Students import Student
from domains.Course import Course
stdscr = curses.initscr()
def input_students(self):
        current_row = int(10)
        date_partern = r"([0-9]{2})/([0-9]{2})/([0-9]{4})"
        stdscr.addstr( current_row, 0, "Enter the number of students: ")
        stdscr.refresh()
        curses.echo()
        student_num = stdscr.getstr()
        y,x = stdscr.getyx()
        while not student_num.isdigit():
            stdscr.move(y-1, x)
            stdscr.clrtoeol()
            stdscr.addstr("Enter the valid number:")
            stdscr.refresh()
            curses.echo()
            student_num = stdscr.getstr()
        student_num = int(student_num)
        for _ in range(student_num):
            stdscr.addstr("Enter the id of student: ")
            stdscr.refresh()
            curses.echo()
            id = stdscr.getstr()
            stdscr.addstr("Enter the name of student:")
            stdscr.refresh()
            curses.echo()
            name = stdscr.getstr()
            stdscr.addstr("Enter the DoB of student(DD/MM/YYYY):")
            stdscr.refresh()
            curses.echo()
            DoB = stdscr.getstr()
            y,x = stdscr.getyx()
            while not re.match(date_partern, DoB.decode()):
                stdscr.move(y-1, x)
                stdscr.clrtoeol()
                stdscr.addstr("Enter the valid DoB of student(DD/MM/YYYY): ")
                stdscr.refresh()
                curses.echo()
                DoB = stdscr.getstr()
            self.students[id] = Student(id, name, DoB)
            stdscr.addstr("Student added")
            stdscr.refresh()
            stdscr.getch()
#write student information to file
            with open("students.xtlm", "a") as f:
                for student in self.students.values():
                    f.write(student.id.decode() + " " + student.name.decode() + " " + student.DoB.decode()+"\n")
def input_courses(self):    
    current_row = int(10)
    stdscr.addstr( current_row, 0, "Enter the number of courses: ")
    stdscr.refresh()
    curses.echo()
    course_num = stdscr.getstr()
    y,x = stdscr.getyx()
    while not course_num.isdigit():
        stdscr.move(y-1, x)
        stdscr.clrtoeol()
        stdscr.addstr("Enter the valid number:")
        stdscr.refresh()
        curses.echo()
        course_num = stdscr.getstr()
    course_num = int(course_num)
    for _ in range(course_num):
        stdscr.addstr("Enter the id of course: ")
        stdscr.refresh()
        curses.echo()
        id = stdscr.getstr()
        stdscr.addstr("Enter the name of course:")
        stdscr.refresh()
        curses.echo()
        name = stdscr.getstr()
        stdscr.addstr("Enter the credit of course:")
        stdscr.refresh()
        curses.echo()
        credit = stdscr.getstr()
        y,x = stdscr.getyx()
        while not credit.isdigit():
            stdscr.move(y-1, x)
            stdscr.clrtoeol()
            stdscr.addstr("Enter the valid number:")
            stdscr.refresh()
            curses.echo()
            credit = stdscr.getstr()
        credit = int(credit)
        self.courses[id] = Course(id, name, credit)
        stdscr.addstr("Course added")
        stdscr.refresh()
        stdscr.getch()
        #write course information to file:
        with open("courses.txt", "a") as f:
            for course in self.courses.values():
                f.write(course.id.decode() + " " + course.name.decode() + " " + str(course.credit)+"\n")
def input_marks(self):
    self.list_courses()
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
    student = self.students[student_id]
    stdscr.addstr("Enter the mark of student: ")
    stdscr.refresh()
    curses.echo()
    mark = stdscr.getstr()
    y,x = stdscr.getyx()
    while not mark.isdigit():
        stdscr.move(y, x)
        stdscr.clrtoeol()
        stdscr.addstr("Enter the valid number:")
        stdscr.refresh()
        curses.echo()
        mark = stdscr.getstr()
    mark = int(mark)
    course.students[student_id] = student
    student.marks[course_id] = mark
    stdscr.addstr("Mark added")
    stdscr.refresh()
    stdscr.getch()
    #write mark information to file:
    with open("marks.txt", "a") as f:
        f.write(course_id.decode() + " " + student_id.decode() + " " + str(mark)+"\n")

