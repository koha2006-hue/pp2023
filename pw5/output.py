import curses
import re
stdscr = curses.initscr()
class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
        self.marks = {}
        self.GPA = 0

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.students = {}
        self.credit = credit

class Manager:
    def __init__(self):
        self.students = {}
        self.courses = {}
    def reset_screen(self):
        stdscr.clear()
        self.menu()
        stdscr.refresh()
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

#Menu:
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
                            break
                        else:
                            exit()
                    print_menu(stdscr,current_row)
                    stdscr.refresh()
            curses.wrapper(main)
