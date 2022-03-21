from enum import Enum
from uuid import uuid4

class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class Person:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.dob = None
        self.alive = None

    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_dob(self, dob):
        self.dob = dob

    def update_status(self, alive):
        self.alive = alive

class Instructor(Person):
    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)
        self.instructor_id = f'Instructor_{uuid4()}'

class Student(Person):
    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)
        self.student_id = f'Student_{uuid4()}'

class ZipCodeStudent(Student):
    def __init__(self, first_name, last_name, dob, alive, student_id):
        super().__init__(first_name, last_name, dob, alive, student_id)

class CollegeStudent(Student):
    def __init__(self, first_name, last_name, dob, alive, student_id):
        super().__init__(first_name, last_name, dob, alive, student_id)

class Classroom:
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor):
