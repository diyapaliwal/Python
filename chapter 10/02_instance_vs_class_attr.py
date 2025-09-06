class employee():
    language = "Python"  # class attribute
    salary = 1200000
    
diya = employee()
diya.name = "Diya Paliwal"  # instance attribute
#here name is am instance attribute and salary anmd language are class attributes as they directly belong to the class.
print(diya.name, diya.language, diya.salary )

Manas = employee()
Manas.language = "Java"    # Instance attributes, take preference over class attributes during assignment & retrieval.

print(Manas.language, Manas.salary)