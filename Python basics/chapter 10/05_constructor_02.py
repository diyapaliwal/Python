class Employee:
    l = "p"
    s = 10000
    
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