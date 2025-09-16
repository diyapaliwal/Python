# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def __init__(self):
        print("there are different types of animals")

class Pets(Animals):
    def __init__(self):
        super().__init__()
        print("Some animals can be pets")

class Dog(Pets):
    @staticmethod
    def bark():
        print("The dogs are one of the pet type animal who bark")
    
d  = Dog()
d.bark()