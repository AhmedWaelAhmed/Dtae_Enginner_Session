# department.py
from typing import List
from patiant import Patient
from staff import Staff

class Department:
    def __init__(self, name: str):
        self.name = name
        # "manages *" relationship -> List of Patients
        self.patients: List[Patient] = []
        # "employs *" relationship -> List of Staff
        self.staff_members: List[Staff] = []

    def add_patient(self, patient: Patient) -> None:
        # Matches UML: add_patient(patient: Patient): void
        self.patients.append(patient)
        print(f"Patient {patient.name} added to {self.name}.")

    def add_staff(self, staff_member: Staff) -> None:
        # Matches UML: add_staff(staff_member: Staff): void
        self.staff_members.append(staff_member)
        print(f"Staff {staff_member.name} added to {self.name}.")