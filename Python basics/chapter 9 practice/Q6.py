with open("log.txt") as f:
    content = f.read()
    
if "python" in content:
    print("yes this code contain python word!")
    
else:
    print("There is no python word")