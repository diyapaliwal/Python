# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
class xyz:
    a = 123
        
obj = xyz()
obj.a = 0
print(obj.a)

# yes it changed the class attribute as we all know that instance atrribute is prioritised