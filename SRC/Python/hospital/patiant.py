# patient.py
from person import Person

class Patient(Person):
    def __init__(self, name: str, age: int, medical_record: str):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self) -> str:
        # Returns a string as per UML: "view_record(): String"
        return f"Patient: {self.name}, Record: {self.medical_record}"