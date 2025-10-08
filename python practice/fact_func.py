num = int(input())

def fact(num):
    fact = 1
    while num!=0:
        fact*=num
        num-=1
    return fact
    
print(fact(num))