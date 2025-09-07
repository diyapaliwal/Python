# Add a static method in problem 2, to greet the user with hello.
import math
class calculator:
    @staticmethod
    def greet():
        print("HEllO!")
    def square(self,num):
        print(f"square of {num} = {num**2}")
    def cube(self,num):
        print(f"Cube of {num} = {num**3}")
    def sqrt(self,num):
        print(f"Square root of {num} = {math.sqrt(num)}")
        
num = int(input("enter a number: "))

a = calculator()
a.greet()
a.square(num)
a.cube(num)
a.sqrt(num)