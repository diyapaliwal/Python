class employee:
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"{self.name} and works at {self.company}")
        
class programmer(employee):
    company = "ITC infotech"
    language = "Python"
    def showLang(self):
        print(f"{self.name} and is good in {self.language}at {self.company}")
        
a= employee()
b= programmer()

print(a.company, b.company)

b.show()
b.showLang()