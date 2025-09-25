def fun(*number):
    print(number,type(number))
    print(sum(number))
a = int(input())
b = int(input())

fun(a,b,3,4) # we can pass as many arguments we want to and number will store them in a tuple without specifying parameters there.