class Employee():
    language = "Python"
    salary = 1200000
    
    def getInfo(self): # we have to add self here as an attribute sot hat it runs without error and at place of self you can add any other word but self is recognisable word
        print(f"{self.name} is expert in {self.language} and earns {self.salary} per year.")
        
    # def greet():  # This will give error of 0 positional argument
    #     print("whats this rubish")
    # this can be cured using @staticmethod
    @staticmethod   #it do not give error or dont need self
    def greet():
        print("or bhai kya haal!")
    
    
Diya = Employee()
Diya.name = "Diya Paliwal"
Diya.getInfo()
Diya.greet()
# Employee.getInfo(Diya)  #alternative method to use Diya.getInfo()