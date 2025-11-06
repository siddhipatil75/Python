4.Destructor
class Student:
    def __init__(self, name):
        self.name = name
        print(f"Constructor Called for {self.name}")

    def __del__(self):
        print(f"Destructor Called for {self.name}")

# Creating object
s1 = Student("Vaishnavi")

# Deleting object manually
del s1

print("End of Program")