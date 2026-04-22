import sys
import gc

class Student:

    class Course:
        def __init__(self, course_name, course_code):
            self.course_name = course_name
            self.course_code = course_code

        def display_course(self):
            print(f"Course: {self.course_name} (Code: {self.course_code})")

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.courses = []  # List to store enrolled courses
        print(f"Student {self.student_name} (ID: {self.student_id}) has registered.")

    def enroll_course(self, course_name, course_code):
        new_course = Student.Course(course_name, course_code)
        self.courses.append(new_course)
        print(f"Student {self.student_name} enrolled in {course_name}.")

    def display_student_info(self):
        print(f"\nStudent ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print("Enrolled Courses:")
        for course in self.courses:
            course.display_course()

    def __del__(self):
        print(f"Student {self.student_name} (ID: {self.student_id}) has been deregistered.")

student1 = Student(101, "Alice")

student1.enroll_course("Mathematics", "MATH101")
student1.enroll_course("Physics", "PHY101")

student1.display_student_info()

print("\nReference Count for student1 object before deletion:", sys.getrefcount(student1))

del student1

gc.collect()
