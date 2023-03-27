import curses
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