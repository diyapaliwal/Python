n = int(input("Enter a number: "))

def fun(n):
    if(n==1):
        print("*")
        return
    print("*" * n)
    fun(n-1)
    
fun(n)