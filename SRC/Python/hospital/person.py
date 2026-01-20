# person.py
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def view_info(self) -> str:
        # Returns a string as per UML: "view_info(): String"
        return f"Name: {self.name}, Age: {self.age}"