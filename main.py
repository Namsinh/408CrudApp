# Monique Namsinh
# 02/27/2019
# CPSC408 Database Mgmt
# 1856274

import sqlite3
from Student import Student


def main():

    create_table()
    display_menu()

    user_choice = int(input('Choose a query #1-5: '))
    choice = True
    while choice:
        if user_choice > 5:
            user_choice = int(input('Invalid choice, try again #1-5: '))
        else:
            print "Choice: %d", user_choice
            choice = False
    if user_choice == 1:
        view_table()
    elif user_choice == 2:
        sid = raw_input('Enter new student ID:')
        first = raw_input("Enter first name:")
        last = raw_input('Enter last name:')
        gpa = raw_input('Enter GPA:')
        major = raw_input('Enter major:')
        faculty = raw_input('Enter faculty advisor:')
        insert_record(sid, first, last, gpa, major, faculty)
    elif user_choice == 3:
        newmajor = raw_input('Enter updated major:')
        newfaculty = raw_input('Enter updated faculty advisor:')
        update_record(newmajor, newfaculty)
    elif user_choice == 4:
        sid = int(input('Enter SID of record to delete:'))
        delete_record(sid)
    elif user_choice == 5:
        major = raw_input('Enter major, or enter to continue:')
        gpa = float(input('Enter gpa, or enter to continue:'))
        advisor = raw_input('Enter faculty advisor, or enter to continue:')
        display_record(major, gpa, advisor)
    elif user_choice == 6:
        exit()
