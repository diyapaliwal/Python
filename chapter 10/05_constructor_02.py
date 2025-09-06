class Employee():
    l = "p"
    s = 10000
    ''' 1)__init__() is a special method which is first run as soon as the object is created.
    2) __init__() method is also known as constructor.
    3) It takes ‘self’ argument and can also take further arguments.'''
    
    def __init__(self):  # works without calling
        print("This is a constructor.")
        
    def __init__(self,name,s,l):
        self.name = name
        self.s = s
        self.l = l
        print(f"{name} earns in lakhs aprox. {s}rs just by learning {l}")
        
manas = Employee()
manas.name = "Manas Paliwal"
print(manas.name,manas.l, manas.s)