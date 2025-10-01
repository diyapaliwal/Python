pw = input("Enter password \n")

if(len(pw)>=8 and any(ch.isdigit() for ch in pw)):
    print("Strong Password")
    
else:
    print("Weak Password")