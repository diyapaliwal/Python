# Create a class ‘Employee’ and add salary and increment properties to it. Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 234
    inc = 20
    
    @property
    def SAI(self):
        self.newSalary = (self.salary + (self.salary * self.inc)/100)
        return self.newSalary
    
    @SAI.setter
    def SAI(self,value):
        print(value)
        self.increment = ((value-self.salary)/self.salary)*100
    
e = Employee()
e.SAI = 300
print(e.increment)