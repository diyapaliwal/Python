class Employee:
    l = "p"
    s = 10000
    ''' 1)__init__() is a special method which is first run as soon as the object is created.
    2) __init__() method is also known as constructor.
    3) It takes ‘self’ argument and can also take further arguments.'''
    
    def __init__(self):  # works without calling also known as dunder method
        print("This is a constructor.")
        
manas = Employee()
manas.name = "Manas Paliwal"
print(manas.name,manas.l, manas.s)