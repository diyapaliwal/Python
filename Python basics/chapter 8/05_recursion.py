# factorial(0) = 1
# factorial(1) = 1
# factorial(2) = 1*2

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n* factorial(n-1)

n = int(input("enter a number n: "))
print(factorial(n))