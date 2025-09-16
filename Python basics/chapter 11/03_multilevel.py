class employee:
    name = "diya"
    company = "itc"
    def show(self):
        print(f"{self.name} works at {self.company}")
        
class job(employee):
    role= "Python Developer"
    def jobRole(self):
        print(f"employee {self.name} is selcted for job role as {self.role}")
        
class programmer(job):
    def overall(self):
        print(f"{self.name} works as a {self.role} at {self.company}")
  
b = job()
b.show()
b.jobRole()
      
c = programmer()
c.show()
c.jobRole() 
c.overall()