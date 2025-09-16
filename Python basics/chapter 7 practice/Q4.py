import math
i = int(input("Enter the number: "))

if i < 2:
    print("not prime")
    
for j in range(2,int(math.sqrt(i))+1):
    if(i%j ==0):
        print("not prime")
        break
else:
    print("prime")