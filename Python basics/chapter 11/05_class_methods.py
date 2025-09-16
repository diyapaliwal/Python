class employee:
    a=1
    def show(self):
        print(f"The class value of a is {self.a}")
        
o = employee()
o.a = 45 
o.show() # shows the inheritance value of a

# but we want the class attribute's value
class programmer:
    a=1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")
        
o = programmer()
o.a = 45
o.show()