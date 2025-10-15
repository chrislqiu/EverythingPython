"""
A single file can contain multiple classes, but it's a good practice to keep one class per file for better organization and readability.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # This is ran when we try to print he entire obj
    def __str__(self):
        # Use f to format and insert variable by using {}
        return f"My name is {self.name} and I am {self.age} years old."

# Creating an obj
p1 = Person("Chris", 22)
print(f"This is me printing the obj: {p1}")

p1.age = 21
print(f"This is age after modification: {p1.age}")

"""
INHERITANCE
"""

class Student(Person):
    # We can also add more properties to the Student class like id
    def __init__(self, name, age, id):
        # Inherits the properties and methods from Person
        super().__init__(name, age)
        self.id = id
    
    def __str__(self):
        return f"Welcome {self.name}, you are {self.age} years old and your student ID is {self.id}."
    
s1 = Student("Chris", 22, "2943")
print(f"This is student obj: {s1}")