# Write a program to make a copy of a text file “this. txt”

with open("Q8_this.txt") as f:
    content = f.read()
    
with open("Q8_copy.txt","w") as f:
    f.write(content)
    
# shorter version

# with open("Q8_this.txt") as f , open("Q8_copy.txt","w") as copy:
#     for line in f:
#         copy.write(line)