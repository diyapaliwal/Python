from functools import reduce
# Map Example
L = [1,2,3,4,5,6]

sq = lambda x: x*x

sqList = map(sq,L)
print(list(sqList))

#filter example
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even,L)
print(list(onlyEven))

#reduce Function
def sum(a,b):
    return a+b

mul = lambda x,y:x*y

print(reduce(sum,L))
print(reduce(mul,L))