m1= int(input("enter marks of maths: "))
m2= int(input("enter marks of physics: "))
m3= int(input("enter marks of chemistry: "))

if((m1/100)*100>33 and (m2/100)*100>33 and (m3/100)*100>33 and (m1+m2+m3)/300*100>40):
    print("Pass")
else:
    print("Fail")