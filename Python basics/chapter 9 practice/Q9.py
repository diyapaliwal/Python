# Write a program to find out whether a file is identical & matches the content of another file.

with open("Q8_this.txt") as f:
    content1= f.read()
    
with open("Q8_copy.txt") as f:
    content2= f.read()
    
if content1 == content2:
    print("identical file")
    
else:
    print("not an identical file")