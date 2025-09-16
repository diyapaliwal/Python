a = int(input("Enter your age: "))
if(a>=18):
    print("you can vote")
elif(a<0):
     print("Age cant be -ve")
elif(a==0):
    print("Age cant be 0")
else:
    print("you can't vote")