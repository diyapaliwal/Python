# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
class vector:
    def __init__(self, x,y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self,v2):
        sum = ((self.x + v2.x),(self.y + v2.y),(self.z + v2.z))
        return sum
    
    def __mul__(self,v2):
        product = ((self.x * v2.x)+(self.y * v2.y)+(self.z * v2.z))
        return product
    
v1 = vector(1,2,3)
v2 = vector(4,5,6)
print("v1 + v2 =",v1+v2)
print("v1.v2 =",v1*v2)