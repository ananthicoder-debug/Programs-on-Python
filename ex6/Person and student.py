class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Person Name: {self.name}\nAge: {self.age}")
        print("--------------------")

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display(self):
        print(f"Student Name: {self.name}\nAge: {self.age}")
        print(f"ID: {self.student_id}\nCourse: {self.course}")
        print("--------------------")

class Faculty(Person):
    def __init__(self, name, age, faculty_id, department):
        super().__init__(name, age)
        self.faculty_id = faculty_id
        self.department = department

    def display(self):
        print(f"Faculty Name: {self.name}\nAge: {self.age}")
        print(f"ID: {self.faculty_id}\nDepartment: {self.department}")

people = [
    Person("Shalu", 30),
    Student("Malu", 20, "S101", "IT"),
    Faculty("Dolu", 45, "F202", "Mathematics")
]

for person in people:
    person.display()
