# Write a program to find out the line number where python is present from ques 6

with open("Q7_log.txt") as f:
    lines = f.readlines()
    
lineno=1
found = False
a=[]
for line in lines:
    if "python" in line.lower():
        # print(f"python is present in line {lineno}")
        a.append(lineno)
        found = True
    lineno += 1
if found:
    print(f"the word was present in line {a}")
    
if not found:
    print("python word do not exist.")