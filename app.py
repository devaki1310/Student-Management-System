from view import DatabaseOperations
def menu():
    while(True):
        print()
      

        print("**********Welcome to Student Management System Project**********")
        print(f"\t 1:Add Student \n \t 2:Update Student \n \t 3: Delete Student \n \t 4:Display All Student \n \t 5:Find Student By Roll Number \n \t 6:Exit")
        print()

        choice =eval(input("Enter Your Choice:"))
        print()

        if (choice==1):
            DatabaseOperations.add_student()
        elif(choice==2):
            DatabaseOperations.update_student()
        elif(choice==3):
            DatabaseOperations.delete_student()
        elif(choice==4):
            DatabaseOperations.display_all_student()
        elif(choice==5):
            rollnum = int(input("Enter Roll Number to Search: "))
            result = DatabaseOperations.find_student_by_rollnum(rollnum)
    
            if result is not None:
                result.display()

            else:
                print("Student found")
        else:
            print("Exit")
            break


menu()


