# Override the __len__() method on vector of problem 5 to display the dimension of the vector
class vector:
    def __init__(self,l):
        self.l = l
        self.x = l[0]
        self.y = l[1]
        self.z = l[2]
    
    def __add__(self,v2):
        sum = ((self.x + v2.x),(self.y + v2.y),(self.z + v2.z))
        return sum
    
    def __mul__(self,v2):
        product = ((self.x * v2.x)+(self.y * v2.y)+(self.z * v2.z))
        return product
    
    def __len__(self):
        return len(self.l)
    
v1 = vector([1,2,3])
v2 = vector([4,5,6])
print("v1 + v2 =",v1+v2)
print("v1.v2 =",v1*v2)
print(len(v1))