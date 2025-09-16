''' A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file.'''
with open("Q4_file.txt") as f:
    content = f.read()
    
newCon = content.replace("donkey", "######")

with open("Q4_file.txt","w") as f:
    f.write(newCon)