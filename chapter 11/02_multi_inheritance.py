class employee:
    name = "diya"
    company = "itc"
    def show(self):
        print(f"{self.name} works at {self.company}")
        
class job:
    role= "Python Developer"
    def jobRole(self):
        print(f"job roles available here are {self.role}")
        
class programmer(employee, job):
    def overall(self):
        print(f"{self.name} works as a {self.role} at {self.company}")
        
a = programmer()
a.overall()