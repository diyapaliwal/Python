# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Vector_2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        return f"2D Vector: ({self.x},{self.y})"
    
class Vector_3D(Vector_2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
        
    def show(self):
        return f"3D Vector: ({self.x},{self.y},{self.z})"
    
V1 = Vector_2D(1,2)
print(V1.show())

V2 = Vector_3D(1,2,3)
print(V2.show())