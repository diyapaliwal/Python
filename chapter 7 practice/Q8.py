num = int(input("Enter the number of rows: "))

for i in range(1,num+1):
    print(" "* (num-i), end="")
    print("*"*(2*i-1))
    # print("\n")