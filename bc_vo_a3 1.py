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

class UserMenuInterface:
    def __init__(self) -> None:
        pass
    # TODO: add required methods.


class StudentDBInterface:
    def __init__(self, db_file="students.db", json_file="stds_initial_data.json"):
        print("initializing init")
        # TODO: complete the method
        # Fields 
        self.db_file = db_file
        self.json_file = json_file
        self.Database = None
        self.querydatabase = None
        
        # NOTES: Read the Json file
        print("Reading Json file")
        with open(json_file, "r") as file:
            jsondata = json.load(file)
        
        # NOTES: Make database or connect to database
        print("Making database or connecting to database")
        self.Database = sqlite3.connect(db_file)

        # NOTES: Query database can execute SQL commands
        print("Ready Querying database")
        self.querydatabase = self.Database.cursor()


    def create_table(self):
        # TODO: complete the method
        print("Creating table")
        # Check if table exists
        try:
            print("Executing query - check if table exists")
            self.querydatabase.execute("SELECT * FROM students")
        except:
            print("Table does not exist")
            
        finally:
            print("Table does not exist")
        
        query = "CREATE TABLE students (Studentnumber NVARCHAR(8) PRIMARY KEY, FirstName NVARCHAR(50) NOT NULL, LastName NVARCHAR(50) NOT NULL, City NVARCHAR(50), DateOfBirth NVARCHAR(10), Class NVARCHAR(50);"
        # If not create table
        # If exists do nothing
        print("Executing query - create table")
        self.querydatabase.execute(query)  
        print("save changes")
        self.Database.commit()


    def create_table_from_json(self):
        # TODO: complete the method
        pass


    def insert_initial_data(self):
        # TODO: complete the method
        pass

    def add_new_student(self, first_name, last_name, city, date_of_birth=None, class_=None):
        # TODO: complete the method
        pass
        query = "INSERT INTO students (FirstName, LastName, City, DateOfBirth, Class) VALUES ({}, {}, {}, {}, {});"

    def assign_student_to_class(self):
        # TODO: complete the method
        pass

    def list_all_students(self):
        # TODO: complete the method
        pass

    def list_students_in_class(self):
        # TODO: complete the method
        pass

    def search_student(self):
        # TODO: complete the method
        pass

    def quit_program(self):
        # TODO: complete the method
        pass

if __name__ == "__main__":
    # TODO: complete the main function.
    print("Starting program")
    randomvar = StudentDBInterface()
    randomvar.create_table()



    # Closing the connection
    randomvar.Database.close()
    print("Database closed")





