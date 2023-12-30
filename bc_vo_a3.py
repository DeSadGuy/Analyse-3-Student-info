'''
Implement a Python program to solve the following problem statement:

In this problem you are going to create an program to organise students and their info by class. 
The program will read a data file (provided as json file within the same folder) and fill / update a database (sqlite 3.x).
If the database does not exist, then the program must first create a proper table based on the attributed extracted from the provided json file. 
The program must use proper try-except structures to handle common exceptions. In case of any exception, the program must print a proper error message and quit.
If the launch of the program is successful, then the following menu will appear to interact with the user:

[A] Add new student
    > should ask for: first_name, last_name, city, date_of_birth (DD-MM-YYYY), class (optional)
    > should return the assigned student number. Student numbers must be generated automatically and be unique, with length=7, starting with 09 .
[C] Assign student to a class
    > should ask for: student number (primary_key), class
    > should give error if student was not found: Could not find student with number: {student number}
[D] List all students
    > result should be sorted based on class in descending order
[L] List all students in class
    > should ask for class to search students in
    > result should be sorted based on studentnumber in ascending order
[S] Search student
    > should ask for search term and search in first_name, last_name or city
    > limit result to 1
[Q] Quit
    > replace the initial json file with a new one containing latest values of the database. The structure of the json file must not change.

Criteria:
- The program must be implemented using basics of Object Oriented Programming in Python. Applying full featured object oriented programming (like inheritance, polymorphism, static methods, etc) is not mandatory.
- Divide the functionality of your program between two classes (given below as the template): UserMenuInterface is responsible for interactions between the user and the program with proper messages, StudentDBInterface is responsible for interactions with the db.
- There must be a separate file, named as test_bc_vo_a3.py, where a unit test is implemented. For unit tests use PyTest. 
- In the unit test, there must be two functions named test_add_new_student(...) and test_assign_student_to_class(...).
- Feel free to add extra methods / parameters wherever you see it is necessary.
- Add your student number here before submitting your solution: student number =  [here] .
'''

import sqlite3
import json
import time
import random

class UserMenuInterface:
    def __init__(self) -> None:
        pass
    # TODO: add required methods.
    
    def show_menu(self):
        string = """
            [A] add new student
            [C] assign student to a class
            [D] list all students
            [L] list all students in class
            [S] search student
            [Q] quit
            """
        print(string)
    def get_user_choice(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")
            choice = choice.upper()
            choice = choice.strip()
            if choice == "A":
                self.add_new_student()
            elif choice == "C":
                self.assign_student_to_class()
            elif choice == "D":
                self.list_all_students()
            elif choice == "L":
                self.list_students_in_class()
            elif choice == "S":
                self.search_student()
            elif choice == "Q":
                self.quit_program()
            else:
                print("Invalid input")
                self.get_user_choice()

    def add_new_student(self):
        print("...")
        print("Adding new student")
        print("Enter first name")
        first_name = input("Enter your input: ")
        print("Enter last name")
        last_name = input("Enter your input: ")
        print("Enter city")
        city = input("Enter your input: ")
        print("Enter date of birth (DD-MM-YYYY)")
        date_of_birth = input("Enter your input: ")
        print("Enter class")
        class_ = input("Enter your input: ")
        print("Processing")
        database.add_new_student_without_studentnumber(first_name, last_name, city, date_of_birth, class_)
        print("DONE")

    def assign_student_to_class(self):
        print("...")
        print("Assigning student to class")
        print("Enter student number")
        studentnumber = input("Enter your input: ")
        studentnumber = studentnumber.strip()
        print("Enter class")
        class_ = input("Enter your input: ")
        print("Processing")
        database.assign_student_to_class(studentnumber, class_)
        print("DONE")
        

    def list_all_students(self):
        print("...")
        print("Listing all students")
        print("Processing")
        database.list_all_students()
        print("DONE")

    def list_students_in_class(self):
        print("...")
        print("Listing students in class")
        print("Enter class")
        class_ = input("Enter your input: ")
        print("Processing")
        database.list_students_in_class(class_)
        print("DONE")

    def search_student(self):
        print("...")
        print("Searching for student")
        print("Enter search term")
        search_term = input("Enter your input: ")
        print("Processing")
        database.search_student(search_term)
        print("DONE")

    def quit_program(self):
        print("...")
        print("Quitting program")
        print("Processing")
        database.quit_program()
        print("DONE")


    
class StudentDBInterface:
    def __init__(self, db_file="students.db", json_file="stds_initial_data.json"):
        print("initializing init")
        # TODO: complete the method
        # Fields 
        self.db_file = db_file
        self.json_file = json_file
        self.Database = None
        self.querydatabase = None
        self.jsondata = None
        
        # NOTES: Read the Json file
        print("Reading Json file")
        with open(json_file, "r") as file:
            jsondata = json.load(file)
            self.jsondata = jsondata

        # NOTES: Make database or connect to database
        print("Making database or connecting to database")
        self.Database = sqlite3.connect(db_file)

        # NOTES: Query database can execute SQL commands
        print("Ready Querying database")
        self.querydatabase = self.Database.cursor()
        print("DONE")

    def check_if_table_exists(self):
        print("...")
        print("Checking if table exists")
        table_name = "students"
        query = f"SELECT name FROM sqlite_master WHERE type='table'"
        self.querydatabase.execute(query)
        # NOTES: Fetchall returns a list of tuples
        result = self.querydatabase.fetchall()
        if (table_name,) in result:
            print("Table exists")
            print("checkin if table exist DONE")
            return True
        else:
            print("Table does not exist")
            print("checking if table exist DONE")
            return False

    def create_table(self):
        # TODO: complete the method
        print("...")
        print("Creating table")
        # NOTES: Check if table exists
        if self.check_if_table_exists():
            print("Table already exists")
            return

        # NOTES: Create table
        query = "CREATE TABLE IF NOT EXISTS students (Studentnumber TEXT PRIMARY KEY, Firstname TEXT, Lastname TEXT, City TEXT, Dateofbirth TEXT, Class TEXT)"
        self.querydatabase.execute(query)
        self.Database.commit()
        print("Table DONE")


    def create_table_from_json(self):
        # TODO: complete the method
        print("...")
        print("Creating table from json file")
        self.create_table()
        print("...")
        self.insert_initial_data()
        print("create table from json DONE")

        

    def insert_initial_data(self):
        # TODO: complete the method
        print("...")
        print("Inserting initial data from json file")
        list_of_students = self.jsondata["students"]
        for student in list_of_students:
            self.add_new_student(student["studentnumber"], student["first_name"], student["last_name"], student["city"], student["date_of_birth"], student["class"])
        print("insert initial data DONE")

    def add_new_student(self, studentnumber ,first_name, last_name, city, date_of_birth, class_=None):
        print("...")
        print("Adding new student")
        print("Checking if student number exists")
        query = f"SELECT * FROM students WHERE Studentnumber = '{studentnumber}'"
        self.querydatabase.execute(query)
        result = self.querydatabase.fetchall()
        if result:
            # NOTES: Student number exists
            print("Student already exists")
        else:
            # NOTES: Insert new student
            print("Student does not exist")
            print("Inserting new student")
            query = f"INSERT INTO students VALUES ('{studentnumber}', '{first_name}', '{last_name}', '{city}', '{date_of_birth}', '{class_}')"
            print(f"'{studentnumber}', '{first_name}', '{last_name}', '{city}', '{date_of_birth}', '{class_}'")
            self.querydatabase.execute(query)
            self.Database.commit()
        print("adding student DONE")

    def add_new_student_without_studentnumber(self, first_name, last_name, city, date_of_birth, class_=None):
        # TODO: complete the method
        print("...")
        print("Adding new student")
        # NOTES: Generate student number
        print("Generating student number")
        studentnumber = "09" + str(random.randint(1000000, 9999999))
        print(studentnumber)
        # NOTES: check if student number exists
        print("Checking if student number exists")
        query = f"SELECT * FROM students WHERE Studentnumber = '{studentnumber}'"
        self.querydatabase.execute(query)
        result = self.querydatabase.fetchall()
        if result:
            # NOTES: Student number exists
            print("Student number exists")
            print("RETRYING")
            self.add_new_student(first_name, last_name, city, date_of_birth, class_)
            print("DONE RETRYING")
        else:
            # NOTES: Insert new student
            print("Student number does not exist")
            print("Inserting new student")
            query = f"INSERT INTO students VALUES ('{studentnumber}', '{first_name}', '{last_name}', '{city}', '{date_of_birth}', '{class_}')"

            self.querydatabase.execute(query)
            self.Database.commit()
        print("adding sutdent DONE")

    def assign_student_to_class(self, studentnumber, class_):
        print("...")
        print("Assigning student to class")
        print("Checking if student exists")
        #NOTES: Check if student exists
        query = f"SELECT * FROM students WHERE Studentnumber = '{studentnumber}'"
        self.querydatabase.execute(query)
        result = self.querydatabase.fetchall()
        if result:
            # NOTES: Student exists
            print("Student exists")
            print("Assigning student to class")
            query = f"UPDATE students SET Class = '{class_}' WHERE Studentnumber = '{studentnumber}'"
            self.querydatabase.execute(query)
            self.Database.commit()
        else:
            # NOTES: Student does not exist
            print("Student does not exist")

    def list_all_students(self):
        print("...")
        print("Listing all students")
        query = "SELECT * FROM students"
        self.querydatabase.execute(query)
        result = self.querydatabase.fetchall()
        for student in result:
            print(student)
        print("DONE")


    def list_students_in_class(self, class_):
        print("...")
        print("Listing students in class")
        query = f"SELECT * FROM students WHERE lower(Class) = '{class_}'"
        self.querydatabase.execute(query)
        result = self.querydatabase.fetchall()
        print(result)
        print("DONE")

    def search_student(self, search_term):
        print("...")
        print("Searching for student")
        query = f"SELECT TOP 1 * FROM students WHERE lower(Firstname) = '{search_term}' OR lower(Lastname) = '{search_term}' OR lower(City) = '{search_term}'"
        self.querydatabase.execute(query)
        result = self.querydatabase.fetchall()
        print(result)
        print("DONE")


    def quit_program(self):
        print("...")
        print("Quitting program")
        print("Saving database")
        self.Database.commit()
        print("Closing database")
        self.Database.close()
        print("DONE")
        print("...")
        print("Saving to json file")

        with open(self.json_file, "w") as file:
            json.dump(self.jsondata, file)

        print("Exiting program")
        exit()

if __name__ == "__main__":
    # TODO: complete the main function.
    print("Starting program")
    database = StudentDBInterface()
    interface = UserMenuInterface()
    StudentDBInterface.create_table_from_json(database)
    interface.get_user_choice()



# Closing the connection
database.Database.close()
print("Database closed")





