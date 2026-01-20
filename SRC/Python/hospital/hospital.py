# hospital.py
from typing import List
from department import Department

class Hospital:
    def __init__(self, name: str, location: str, hospital_id: str):
        self.name = name
        self.location = location
        self.hospital_id = hospital_id  # Added per your request
        # "contains *" relationship -> List of Departments
        self.departments: List[Department] = []

    def add_department(self, department: Department) -> None:
        # Matches UML: add_department(department: Department): void
        self.departments.append(department)
        print(f"Department {department.name} added to {self.name} (ID: {self.hospital_id}).")