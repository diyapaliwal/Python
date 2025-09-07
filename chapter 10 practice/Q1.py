class programmer():
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        print(f"{self.name} have salary {self.salary} per month and pin is{self.pin}")
        
p = programmer("Diya", 13000, "245001")
p = programmer("Manas",12345678,"313002")