2.object
class Student:
    def set_data(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)

# Creating object
s1 = Student()
s1.set_data("Vaishnavi", 101)
s1.display()