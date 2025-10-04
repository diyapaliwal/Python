n = int(input("Enter Number: "))
def p1(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print("")
        
def p2(n):
    for a in range(n):
        for b in range(1,n+1):
            print(b,end="")
        print("")
        
def p3(n):
    for c in range(1,n+1):
        for d in range(c):
            print("*",end="")
        print("")
        
p3(n)