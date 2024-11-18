#NAMBOOZE HELLEN NOELINE B20731 S23B38/014
# a) Function to add a student to the student list
def add_student(student_list, student_id, name, age, course):
    # Check for unique student ID
    for student in student_list:
        if student['id'] == student_id:
            print(f"Error: Student with ID {student_id} already exists.")
            return
    # Add student details to the list
    student_list.append({'id': student_id, 'name': name, 'age': age, 'course': course})

# b) Functions to find and remove a student by ID
def find_student_by_id(student_list, student_id):
    for student in student_list:
        if student['id'] == student_id:
            return student
    print(f"Error: Student with ID {student_id} not found!")
    return None

def remove_student_by_id(student_list, student_id):
    for student in student_list:
        if student['id'] == student_id:
            student_list.remove(student)
            print(f"Student with ID {student_id} has been removed.")
            return
    print(f"Error: Student with ID {student_id} not found!")

# c) Base class Person and subclasses Student and Instructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}.")

class Instructor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

# d) Higher-order function to sort students
def sort_students(student_list, key_function):
    return sorted(student_list, key=key_function)

# Demonstration of functionality
if __name__ == "__main__":
    # Initialize student list
    students = []

    # Adding students
    add_student(students, 2, "Hellen", 20, "Computer Science")
    add_student(students, 3, "Leon", 22, "Mathematics")
    add_student(students, 4, "Mary", 21, "Physics") 

    # Finding a student
    student = find_student_by_id(students, 2)
    print(student) 

    # Removing a student
    remove_student_by_id(students, 2)
    remove_student_by_id(students, 2) 

    # Create instances of Student and Instructor
    student1 = Student("Hellen", 20, "Computer Science")
    instructor1 = Instructor("Dr. Pascal", 45, "Physics")

    # Demonstrating polymorphism
    student1.study()
    instructor1.teach()

    # Sorting students by age and name
    sorted_by_age = sort_students(students, key_function=lambda x: x['age'])
    sorted_by_name = sort_students(students, key_function=lambda x: x['name'])

    print("Sorted by Age:", sorted_by_age)
    print("Sorted by Name:", sorted_by_name)