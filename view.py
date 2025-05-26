from models import Student
from db import Database

class DatabaseOperations:
    @staticmethod
    def add_student():
        s1=Student(input("Enter Student Name: "), eval(input("Enter Student Marks: ")),eval(input("Student Roll Number: ")))
        Database.db[s1.rollnum]=s1

        print("Student added successfully")

    @staticmethod
    def update_student():
       rollnum = eval(input("Eneter Student Roll Number To Update:"))

       for x in Database.db:
           if (rollnum==x):
               Database.db[rollnum].name=input("Enter Updated Name: ")
               Database.db[rollnum].marks=input("Enter Updated Marks: ")
               Database.db[rollnum].roll_num=input("Enter Updated Roll Number: ")

               print("Student Updated successfully")
    @staticmethod
    def delete_student():
        rollnum = eval(input("Eneter Student Roll Number To Delete:"))

        for x in Database.db:
           if (rollnum==x):
            del Database.db[x]
            break
           
        print("Student Deleted successfully")
        
    @staticmethod
    def display_all_student():
        for x in Database.db:
            Database.db[x].display()
    

    @staticmethod
    def find_student_by_rollnum(rollnum):
        if rollnum in Database.db:
            Database.db[rollnum].display()
        else:
            return "Student not found"
    
    
          