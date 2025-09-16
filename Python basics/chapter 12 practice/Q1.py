# Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.
files = ["chapter 12 practice/file1.txt", "chapter 12 practice/file2.txt", "chapter 12 practice/file3.txt"]

for filename in files:
    try:
        with open(filename, "r") as f:
            print(f"{filename} opened successfully!")
            print(f.read())
    except Exception as e:
        print(f"{filename} is not present!")
        
print("Thank You!")