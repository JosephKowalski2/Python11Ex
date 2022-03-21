from enum import Enum

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


