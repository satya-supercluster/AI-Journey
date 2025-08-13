class Student:
    def __init__(self, name: str, age: int, roll: str):
        self.name = name
        self.age = age
        self.roll = roll

    def print_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nRoll number: {self.roll}")


st1: Student = Student("Satyam",  20, "2211201110")
st1.print_info()
# Name: Satyam
# Age: 20
# Roll number: 2211201110
