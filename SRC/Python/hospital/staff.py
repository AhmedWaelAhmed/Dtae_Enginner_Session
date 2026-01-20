# staff.py
from person import Person

class Staff(Person):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        self.position = position

    def view_info(self) -> str:
        # Returns a string as per UML: "view_info(): String"
        base_info = super().view_info()
        return f"{base_info}, Position: {self.position}"