# Import built-in modules
from mysql.connector.errors import *
from mysql.connector import *
import sys

# Import required project classes 
sys.path.append("../")
from objects.student import Student
from objects.admins import Admin
from objects.organization import Organization
from objects.recruiter import Recruiter
from objects.internship import Internship
from config import DBUSERNAME, DBPASSWORD

# Class to connect to a given database
class DatabaseInterface() :

    def __init__(self, db_name) :
        # Intitialise connection to database and set up cursor to execute SQL queries
        self.connection = connect(host = "localhost", user = DBUSERNAME, password = DBPASSWORD, database = db_name)
        self.cursor = self.connection.cursor(buffered=True)

        # Create the 'students' table, if already exist then command is ignored
        try: 
            self.cursor.execute("CREATE TABLE students (fullname VARCHAR(100), studentID VARCHAR(36) , degree VARCHAR(100), score TINYINT(100), experience ENUM('surgery', 'dentistry', 'nursing', 'nutrition', 'medicine'), study_mode VARCHAR(100), study_pattern VARCHAR(2))")
        except ProgrammingError as error: 
            pass

        # Create the 'internships' table, if already exist then command is ignored
        try: 
            self.cursor.execute("CREATE TABLE internships (title VARCHAR(50), internshipID VARCHAR(36), organization VARCHAR(50), field ENUM('surgery', 'dentistry', 'nursing', 'nutrition','medicine'), minScore INT(100), candidatesWanted INT(50))")
        except ProgrammingError as error: 
            pass

    # -------------------------------------------  PRESENCE CHECK OPERATIONS -------------------------------------------------------
    
    # Check whether a matching student already exists
    def student_exists(self, student : Student):
        try:
            query = f"SELECT * FROM students WHERE fullname='{student.get_fullname()}'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return len(rows) == 1
        except ProgrammingError as error:
            raise Exception("Error while checking for student presence")

    # Check whether a matching internship already exists
    def internship_exists(self, internship : Internship):
        try:
            query = f"SELECT * FROM internships WHERE title='{internship.get_title()}' AND organization='{internship.get_organization()}'"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return len(rows) == 1
        except ProgrammingError as error:
            raise Exception("Error while checking for internship presence")

    # -------------------------------------------  DELETE OPERATIONS -------------------------------------------------------

    # Delete entry from the 'students' table if object with matching credentials is found
    def delete_student(self, student : Student) :
        if not self.student_exists(student) : 
            raise Exception("Student does not exist")
        try:
            query = f"DELETE FROM students WHERE fullname='{student.get_fullname()}'"
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to delete student from database")
            print(error)

    # Delete entry from the 'employers' table if object with matching credentials is found
    def delete_internship(self, internship : Internship):
        if not self.internship_exists(internship) : 
            raise Exception("Internship does not exist")
        try:
            query = f"DELETE FROM internships WHERE title='{internship.get_title()}' AND organization='{internship.get_organization()}'"
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to delete internship from database")
            print(error)

    # Deletes everything within a given table
    def reset_table(self, table_name):
        try:
            self.cursor.execute(f"DELETE FROM {table_name}")
            self.connection.commit()
            return True
        except ProgrammingError as error:
            message = f"Failed to reset {table_name} table"
            raise Exception(message)
            return False

    # -------------------------------------------  CREATE OPERATIONS  -------------------------------------------------------

    # Create new entry in the 'student' table using input Student object
    def add_student(self, student : Student):
        if self.student_exists(student) : 
            raise Exception("Student with given credentials already exists")
        try:
            query = f"""
            INSERT INTO students (fullname, studentID, degree, score, experience, study_mode, study_pattern)
            VALUES ('{student.get_fullname()}', '{student.get_id()}', '{student.get_degree()}', 
                    '{student.get_score()}', '{student.get_experience()}', '{student.get_study_mode()}', 
                    '{student.get_study_pattern()}')
            """
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to create new student entry")
            print(error)

    # Create new entry in the 'internship' table using input Internship object
    def add_internship(self, internship : Internship):
        if self.internship_exists(internship) : 
            raise Exception("Internship with given credentials already exists")
        try:
            query = f"INSERT INTO internships (title, internshipID, organization, field, minScore, candidatesWanted) VALUES ('{internship.get_title()}', '{internship.get_id()}', '{internship.get_organization()}', '{internship.get_field()}', '{internship.get_minscore()}', '{internship.get_candidates_wanted()}')"
            self.cursor.execute(query)
            self.connection.commit()
        except ProgrammingError as error:
            raise Exception("Failed to create new internship entry")
            print(error)

    # -------------------------------------------  READ OPERATIONS  -------------------------------------------------------

    # Print the contents of a given table
    def get_table(self, table_name):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            return [ row for row in list(self.cursor) ]
        except ProgrammingError as error:
            print("Error while trying to display table data. Make sure table exists")       
            print(error)
        