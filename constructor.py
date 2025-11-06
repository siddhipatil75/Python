3.constructor
class Student:
    # Constructor
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print("Constructor Called")

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)

# Object creation automatically calls constructor
s1 = Student("Vaishnavi", 101)
s1.display()