import sqlite3
import sys


class Student(object):
    def __init__(self, dbpath):
        self.dbpath = 'foobar.db'

    def get_connection(self):
        try:
            conn = sqlite3.connect(self.dbpath)
            print "Successfully connected."
            conn.close()
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(0)

    def display_menu(self):
        print "1.Display All Students"
        print "2.Create New Student"
        print "3.Update Student by Major or Advisor"
        print "4.Delete Student by ID"
        print "5.Display Students by Major, GPA, Advisor"
        print "6.Exit Program"

    def create_table(self):
        conn = sqlite3.connect(self.dbpath)
        # CREATE TABLE
        cur = conn.cursor()
        cur.execute('''CREATE TABLE StudentDB (
        StudentId INTEGER PRIMARY KEY AUTOINCREMENT, 
        FirstName VARCHAR(25),
        LastName VARCHAR(25),
        GPA FLOAT,
        Major VARCHAR(10),
        FacultyAdvisor VARCHAR(25));''')
        print("Table created successfully.")
        conn.commit()
        conn.close()

    def view_table(self):
        conn = sqlite3.connect(self.dbpath)
        cur = conn.cursor()
        cur.execute('''SELECT * FROM StudentDB''')
        rows = cur.fetchall()
        conn.close()
        return rows

    def insert_record(self, sid, first, last, gpa, major, faculty):
        conn = sqlite3.connect(self.dbpath)
        cur = conn.cursor()
        cur.execute('''INSERT INTO StudentDB VALUES (?,?,?,?,?,?);''',
                    (sid, first, last, gpa, major, faculty))  # Need to check for valid input
        conn.commit()
        conn.close()

    def update_record(self, newmajor, newfaculty):
        conn = sqlite3.connect(self.dbpath)
        cur = conn.cursor()
        cur.execute('''UPDATE StudentDB SET Major = ?, FacultyAdvisor = ?;''', (newmajor, newfaculty))
        conn.commit()
        conn.close()

    def delete_record(self, sid):
        conn = sqlite3.connect(self.dbpath)
        cur = conn.cursor()
        cur.execute('''DELETE FROM StudentDB
                    WHERE StudentId = ?;''', sid)
        cur.execute('''SELECT * FROM StudentDB;''')
        rows = cur.fetchall()
        conn.close()
        return rows

    def display_record(self, major, gpa, advisor):
        conn = sqlite3.connect(self.dbpath)
        cur = conn.cursor()
        cur.execute('''SELECT * 
        FROM StudentDB
        WHERE Major=?
        OR GPA=?
        OR FacultyAdvisor=?;''', (major, gpa, advisor))
        rows = cur.fetchall()
        conn.close()
        return rows
