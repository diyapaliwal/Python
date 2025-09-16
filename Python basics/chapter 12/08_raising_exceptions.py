
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
    
if(b == 0):
    raise ZeroDivisionError("we dont entertain 0 as denominator")
else:
    print(f"The division a/b is {a/b}")