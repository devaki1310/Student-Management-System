class Student:
    College_name="NKOCET"
    def __init__(self, name, marks ,rollnum):
        self.name=name
        self.marks=marks
        self.rollnum=rollnum

    def display(self):
        print(f"Student Name is :{self.name}")
        print(f"Student Marks are :{self.marks}")
        print(f"Student Roll Number is :{self.rollnum}")
        print("--"* 10)


    def __str__(self):
        return f"Student[ name={self.name},marks={self.marks},rollnum={self.rollnum} ]"
