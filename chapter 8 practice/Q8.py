n= int(input("Enter a number: "))
def table(n):
    for i in range(1,11):
        print(f"{n}*{i}= {n*i}")
    
print(table(n))