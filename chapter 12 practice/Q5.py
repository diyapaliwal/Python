#  Store the multiplication tables generated in problem 3 in a file named Tables.txt
n = int(input("Enter a number: "))
table = [n*i for i in range(1,11)]
print(table)

with open("chapter 12 practice/Tables.txt","a") as f:
    f.write(f"Table of {n}:{str(table)} \n")
    f.write("\n")