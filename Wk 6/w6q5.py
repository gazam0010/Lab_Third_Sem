#Get student details from the user and store it in a data file

class Student:
    def __init__ (self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    
    def save_in_a_file(self):
        filename = "Marks.data"
        with open(filename, 'a') as file:
            file.write(f"Name: {self.name}, Roll No.: {self.rollno} and Marks: {self.marks}.\n")
        

def input_data():
    name = input("Enter student's name: ")
    rollno = input("Enter student's roll: ")
    marks = input("Enter student's marks: ")
    
    return Student(name, rollno, marks)

num_students = int(input("Enter number of students: "))

for _ in range(num_students):
    print(f"\nEnter  details of student {_+1}: ")

    s = input_data()
    s.save_in_a_file()
    