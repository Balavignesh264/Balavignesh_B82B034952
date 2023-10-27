#Challange 3.2

class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
student1 = Student("Alice", "A001", 3.8)
student2 = Student("Bob", "B002", 3.6)
student3 = Student("Charlie", "C003", 3.9)

student_list = [student1, student2, student3]

sorted_student_list = sort_students(student_list)

for student in sorted_student_list:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")