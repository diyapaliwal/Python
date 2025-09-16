# relational operators also known as comparison operators
a = int(input("enter a number : "))
if(a%2 == 0 and a>0):
    print("a is +ve even")
elif(a%2 == 0 and a<0):
    print("a is -ve even")
else:
    print("a is odd")
    
if(a>=8):
    print("you may go on this ride")
elif(a<=0):
    print("enter a valid age")
else:
    print("this ride is dangerous for you")